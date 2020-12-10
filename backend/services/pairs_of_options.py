from api.models import Model, Criterion, PairsOfOptions, Value, Option, HistoryAnswer
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def create_files(model: object):
    model = Model.objects.get(id=model.id)
    pairs = PairsOfOptions.objects.filter(id_model=model)

    for i in pairs:
        rows = []
        option_1 = i.id_option_1
        option_2 = i.id_option_2
        criterions = Criterion.objects.filter(id_model=model)

        for j in criterions:
            a1 = Value.objects.get(id_option=option_1, id_criterion=j)
            a2 = Value.objects.get(id_option=option_2, id_criterion=j)

            a12 = (a1.value + a2.value) / 2

            # is max
            if j.direction is True:
                a1 = a1.value / a12
                a2 = a2.value / a12

            # is min
            else:
                a1 = 2 - (a1.value / a12)
                a2 = 2 - (a2.value / a12)

            d = a1 - a2 # Разность

            col = [j.number, d]
            rows.append(col)

        rows = _sort(rows)  # Сортируем штобы привести к шкале и нормализуем под проценты

        _init_file(rows, str(i.id), str(model.id))
        _find_winner_many_qriterion(rows, i)  # ищем победителя
        _create_image_for_pair(rows, str(model.id), str(i.id))

    _find_winner_for_model_many(model)


def make_question(model):
    model = Model.objects.get(id=model.id)
    pairs = PairsOfOptions.objects.filter(id_model=model).filter(winner_option=None)
    if not pairs:

        _find_winner_for_model(model)
        Message = {'flag_find_winner': 1, 'model': model.id, 'question': '', 'option_1': 0, 'option_2': 0,
                               'option_1_line': '', 'option_2_line': ''}
        return Message

    else:
        for pair in pairs:
            print('')
            option_1 = pair.id_option_1
            option_2 = pair.id_option_2

            data, delimeter_line, n = _read_file(model, pair)

            if delimeter_line + 1 == n:
                # Данные не разу не сравнивались
                line_first = data[0]
                line_end = data[delimeter_line - 1]

                if line_first[1] != line_end[1]:
                    criteria_number = int(line_first[0])
                    criteria_1 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                    name_1 = criteria_1.name

                    criteria_number = int(line_end[0])
                    criteria_2 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                    name_2 = criteria_2.name

                    question = 'Преимущество по критерию: "' + name_1 + '" важнее чем преимущество по криетрию: "' \
                               + name_2 + '"'
                    Message = {'question': question, 'option_1': option_1.id, 'option_2': option_2.id,
                               'option_1_line': str(0), 'option_2_line': str(delimeter_line - 1), 'model': model.id,
                            'flag_find_winner': 0}

                    return Message


def write_answer(response: dict) -> dict:
    answer: int = response["answer"]
    option_1: int = response["option_1"]
    option_2: int = response["option_2"]
    option_1_line: str = response["option_1_line"]
    option_2_line: str = response["option_2_line"]
    model_id: int = response["model"]
    question: str = response["question"]

    _write_answer_to_history(question, answer, option_1, option_2, model_id)


    model = Model.objects.get(id=model_id)
    pair = PairsOfOptions.objects.filter(id_option_1=option_1).get(id_option_2=option_2)

    data, delimeter_line, n = _read_file(model, pair)

    flag_new_pair = False

    path = 'api/files/models/' + str(model.id) + '/' + str(pair.id) + '.txt'

    if answer == 1:
        # Важнее преимущество по критерию а1

        # Строка состоит из одного критерия или из нескольких, если из одного то -1
        find_delimeter = option_1_line.find(';')

        line = option_1_line + "|" + option_2_line + "|=1\n"
        _write_file(line, path)

        list_2 = option_2_line.split(';')   # Разделили строку по разделителю
        new_line_2 = int(list_2[-1])        # Взяли номер строки самой близкой к центру из списка который сравнивали ранее
        line_end = data[new_line_2 - 1]     # Строку которую мы добавляем
        list_2.append(str(new_line_2-1))
        option_2_line += ';' + str(new_line_2-1)

        list_1 = option_1_line.split(';')
        new_line_1 = int(list_1[-1])
        line_begin = data[new_line_1]

        value_line_end = float(line_end[1])

        if line_begin[0] != line_end[0] and value_line_end != 0.0:

            criteria_number = int(line_begin[0])
            criteria_1 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
            name_1 = criteria_1.name

            name_2 = ''
            first_line = True
            for row in list_2:
                criteria_number = data[int(row[0])][0]
                criteria_2 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                if first_line is True:
                    name_2 = criteria_2.name
                    first_line = False
                else:
                    name_2 += ' и ' + criteria_2.name

        elif value_line_end == 0.0:
                # Если значение с одного края стали равны нулю, а с другого не дошли до центра или до 0
            i = 1
            while (i != 0):
                line_end = data[new_line_2-i]
                if float(line_end[1]) != 0.0:
                    line = option_1_line + "|" + str(new_line_2-i) + "|=2\n"
                    _write_file(line, path)
                    i += 1

                else:
                    break

            _count_winner(model, pair)
            Message = make_question(model)
            flag_new_pair = True

        else:
            # Сошлись к центру  ---0---^
            _count_winner(model, pair)
            Message = make_question(model)
            flag_new_pair = True

    elif answer == 0:
        line = option_1_line + "|" + option_2_line + "|=0\n"
        _write_file(line, path)

        list_2 = option_2_line.split(';')  # Разделили строку по разделителю
        new_line_2 = int(list_2[-1])  # Взяли номер строки самой близкой к центру из списка который сравнивали ранее
        line_end = data[new_line_2-1]

        list_1 = option_1_line.split(';')
        new_line_1 = int(list_1[-1])
        line_begin = data[new_line_1 + 1]

        option_2_line = str(new_line_2-1)
        option_1_line = str(new_line_1 + 1)

        if line_begin[0] == line_end[0] or new_line_1 + 1 == new_line_2:
            # Сошлись к центру  ---0---^
            _count_winner(model, pair)
            Message = make_question(model)
            flag_new_pair = True

        elif line_begin[0] != line_end[0] or new_line_1 + 1 != new_line_2:
            criteria_number = int(line_end[0])
            criteria_2 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
            name_2 = criteria_2.name

            criteria_number = int(line_begin[0])
            criteria_1 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
            name_1 = criteria_1.name


    else:
        # Строка состоит из одного критерия или из нескольких, если из одного то -1
        find_delimeter = option_2_line.find(';')

        if find_delimeter == -1:
            line = option_1_line + "|" + option_2_line + "|=2\n"
            _write_file(line, path)

            list_2 = option_2_line.split(';')  # Разделили строку по разделителю
            new_line_2 = int(list_2[-1])  # Взяли номер строки самой близкой к центру из списка который сравнивали ранее
            line_end = data[new_line_2]

            list_1 = option_1_line.split(';')
            new_line_1 = int(list_1[-1])
            line_begin = data[new_line_1+1]
            list_1.append(str(new_line_1 + 1))
            option_1_line += ';' + str(new_line_1 + 1)

            value_line_begin = float(line_begin[1])
            if line_begin[0] != line_end[0] and value_line_begin != 0.0:
                name_1 = ''
                first_line = True
                for row in list_1:
                    criteria_number = data[int(row[0])][0]
                    criteria_1 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                    if first_line is True:
                        name_1 = criteria_1.name
                        first_line = False
                    else:
                        name_1 += ' и ' + criteria_1.name

                criteria_number = int(line_end[0])
                criteria_2 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                name_2 = criteria_2.name

            elif value_line_begin == 0.0:
                # Если значение с одного края стали равны нулю, а с другого не дошли до центра или до 0

                i = 1
                while (i != 0):
                    line_end = data[new_line_2-i]
                    if float(line_end[1]) != 0.0:
                        line = option_1_line + "|" + str(new_line_2-i) + "|=2\n"
                        _write_file(line, path)

                        i += 1

                    else:
                        break

                _count_winner(model, pair)
                Message = make_question(model)
                flag_new_pair = True

            else:
                # Сошлись к центру  ---0---^
                _count_winner(model, pair)
                Message = make_question(model)
                flag_new_pair = True

        else:
            line = option_1_line + "|" + option_2_line + "|=0\n"
            _write_file(line, path)

            list_2 = option_2_line.split(';')  # Разделили строку по разделителю
            new_line_2 = int(list_2[-1])  # Взяли номер строки самой близкой к центру из списка который сравнивали ранее
            line_end = data[new_line_2]

            list_1 = option_1_line.split(';')
            new_line_1 = int(list_1[-1])
            line_begin = data[new_line_1 + 1]

            option_2_line = str(new_line_2)
            option_1_line = str(new_line_1+1)

            if line_begin[0] != line_end[0]:
                criteria_number = int(line_end[0])
                criteria_2 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                name_2 = criteria_2.name

                criteria_number = int(line_begin[0])
                criteria_1 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                name_1 = criteria_1.name

    if flag_new_pair is False:
        question = 'Преимущество по критерию: "' + name_1 + '" важнее чем преимущество по криетрию: "' \
                   + name_2 + '"'
        Message = {'question': question, 'option_1': option_1, 'option_2': option_2,
                   'option_1_line': option_1_line, 'option_2_line': option_2_line, 'model': model.id,
                   'flag_find_winner': 0}

    return Message


def _read_file(model, pair):
    path = 'api/files/models/' + str(model.id) + '/' + str(pair.id) + '.txt'
    data = []

    with open(path) as f:
        lines = f.readlines()

    # Данные в файле представлены как сначала исходные данные
    # потом cтрока разделитель #####
    # потом данные которые получены в ходе выполнения опросов

    delimeter_line = 0

    n = len(lines)
    for i in range(n):
        if lines[i] == '#####\n':
            delimeter_line = i
            break

        else:
            l = lines[i].split(';')
            l[1] = l[1].split('\n')[0]
            data.append(l)

    return data, delimeter_line, n


def _write_file(line: str, path: str) -> None:
    pair_file = open(path, 'a')  # Открыли файл для записи результатов
    pair_file.write(line)
    pair_file.close()


def _count_winner(model: object, pair: object) -> None:
    path = 'api/files/models/' + str(model.id) + '/' + str(pair.id) + '.txt'

    with open(path) as f:
        lines = f.readlines()

    n = len(lines)
    wins_1 = 0
    wins_2 = 0
    for i in range(n):
        if lines[i].find('|=') != -1:
            temp = lines[i].split('|=')[1].split('\n')[0]
            if int(temp) == 1:
                wins_1 += 1
            else:
                wins_2 += 2

    if wins_1 >= wins_2:
        winner = pair.id_option_1
    else:
        winner = pair.id_option_2

    PairsOfOptions.objects.filter(id=pair.id).update(
        winner_option=winner,
    )


def _find_winner_for_model(model):
    model = Model.objects.get(id=model.id)
    options = Option.objects.filter(id_model=model)
    pairs = PairsOfOptions.objects.filter(id_model=model)

    winners = {}

    for option in options:
        winners[option.id] = 0

    for pair in pairs:
        winner_id = pair.winner_option.id
        winners[winner_id] += 1

    winner_value, winner_id = 0, 0
    for key, value in winners.items():
        if winner_value < value:
            winner_id = key
            winner_value = value

    Model.objects.filter(id=model.id).update(
        id_winner_option_shnur=winner_id,
    )


def _sort(rows: list) -> list:
    # Cортируем пузырьков

    n = len(rows)
    for i in range(n - 1):
        for j in range(n - i - 1):
            row_i = rows[j]
            row_i1 = rows[j + 1]

            if row_i[1] < row_i1[1]:
                rows[j], rows[j + 1] = rows[j + 1], rows[j]

    return rows


def _find_winner_many_qriterion(rows: list, pair: object):
    # Ищем победителя для пары по многокритериальному критерию

    sum = 0
    for row in rows:
        sum += row[1]

    if sum >= 0:
        winner = pair.id_option_1
    else:
        winner = pair.id_option_2

    PairsOfOptions.objects.filter(id=pair.id).update(
        winner_option_many=winner,
    )


def _find_winner_for_model_many(model):
    model = Model.objects.get(id=model.id)
    options = Option.objects.filter(id_model=model)
    pairs = PairsOfOptions.objects.filter(id_model=model)

    winners = {}

    for option in options:
        winners[option.id] = 0

    for pair in pairs:
        winner_id = pair.winner_option_many.id
        winners[winner_id] += 1

    winner_value, winner_id = 0, 0
    for key, value in winners.items():
        if winner_value < value:
            winner_id = key
            winner_value = value

    Model.objects.filter(id=model.id).update(
        id_winner_option_many=winner_id,
    )


def _write_answer_to_history(question, answer, option_1, option_2, model_id):
    model = Model.objects.get(id=model_id)
    option_1 = Option.objects.get(id=option_1)
    option_2 = Option.objects.get(id=option_2)
    pair = PairsOfOptions.objects.get(id_option_1=option_1, id_option_2=option_2)
    if answer == 1:
        HistoryAnswer.objects.create(question=question, answer='Важнее первое', pair=pair, id_model=model)
    elif answer == 2:
        HistoryAnswer.objects.create(question=question, answer='Важнее второе', pair=pair, id_model=model)
    else:
        HistoryAnswer.objects.create(question=question, answer='Одинаково важны', pair=pair, id_model=model)

def _precent(value, max) -> float:
    return value / (max / 100)


def _init_file(data: list, filename: str, modelname: str) -> None:
    path = 'api/files/models/' + modelname + '/' + filename + '.txt'
    pair_file = open(path, 'w')

    for row in data:
        line = ';'.join([str(i) for i in row])
        pair_file.write(line)
        pair_file.write('\n')

    pair_file.write('#####\n')
    pair_file.close()


def _create_image_for_pair(rows, model, pair):
    length = len(rows)
    if length > 10:
        return

    w, h = 480, 480
    interval = int(w / length)   # Интервал между стрелок

    if abs(float(rows[0][1])) > abs(float(rows[length-1][1])):
        max = float(rows[0][1])

    else:
        max = float(rows[length-1][1])

    for row in rows:
        if (max < 0 and float(row[1]) > 0):
            row[1] = int((float(row[1])) * (h/2 - 10) / max * (-1))
        elif (max < 0 and float(row[1]) < 0):
            row[1] = int((float(row[1])) * (h / 2 - 10) / max * (-1))
        else:
            row[1] = int((float(row[1])) * (h / 2 - 10) / max)

    im = Image.new('RGB', (w, h), (195, 197, 200))
    na = np.array(im)

    distance = 15
    h_begin = int(h / 2)
    for row in rows:
        # Draw arrowed line, from 10,20 to w-40,h-60 in black with thickness 8 pixels
        h_end = int(h/2 - (row[1]))
        na = cv2.arrowedLine(na, (distance, h_begin), (distance, h_end), (0, 0, 0), 4)
        distance += interval
    na = cv2.line(na, (0, h_begin), (w, h_begin), (0, 0, 0), 8)

    path = 'api/files/models/' + model + '/' + pair + '.png'
    Image.fromarray(na).save(path)

    # Делаем подписи
    img = Image.open(path)
    idraw = ImageDraw.Draw(img)
    font = ImageFont.truetype('api/files/fonts/9041.ttf', size=18)

    distance = 15
    for row in rows:
        text = str(row[0])
        if float(row[1]) > 0:
            idraw.text((distance, int(h / 2 + 50)), text, font=font, fill='#000000')
        else:
            idraw.text((distance, int(h / 2 - 50)), text, font=font, fill='#000000')
        distance += interval

    p = PairsOfOptions.objects.get(id=int(pair))
    text = p.id_option_2.name
    length = len(text) * 9
    idraw.text((w-15-length, 40), text, font=font, fill='#000000')
    idraw.text((15, h-40), p.id_option_2.name, font=font, fill='#000000')

    img.save(path)