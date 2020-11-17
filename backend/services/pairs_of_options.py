from api.models import Model, Criterion, PairsOfOptions, Value, Option


def create_files(model: object):
    model = Model.objects.get(id=model.id)
    pairs = PairsOfOptions.objects.filter(id_model=model)

    for i in pairs:
        rows = []
        option_1 = i.id_option_1
        option_2 = i.id_option_2
        criterions = Criterion.objects.filter(id_model=model)

        for j in criterions:
            value_obj_1 = Value.objects.get(id_option=option_1, id_criterion=j)
            value_obj_2 = Value.objects.get(id_option=option_2, id_criterion=j)
            max = j.max

            value_1 = _precent(value_obj_1.value, max)
            value_2 = _precent(value_obj_2.value, max)

            if value_1 > value_2:
                difference = value_1 - value_2
            else:
                difference = value_2 - value_1

            if j.direction == True:
                if value_1 > value_2:
                    col = [j.number, difference, 1]
                else:
                    col = [j.number, difference, 2]
            else:
                if value_1 > value_2:
                    col = [j.number, difference, 2]
                else:
                    col = [j.number, difference, 1]

            rows.append(col)

        rows = _sort(rows)   # Сортируем штобы привести к шкале и нормализуем под проценты

        _init_file(rows, i.filename, model.number)


def _precent(value, max) -> float:
    return value / (max / 100)


def _init_file(data: list, filename: str, modelname: str) -> None:
    path = 'api/files/models/' + modelname + '/' + filename + '.txt'
    pair_file = open(path, 'w')

    for row in data:
        line = ';'.join([str(i) for i in row])
        pair_file.write(line)
        pair_file.write('\n')

    pair_file.write('#####')
    pair_file.close()


def _sort(rows: list) -> list:
    s = 1
    for k in range(len(rows) - s):
        for j in range(len(rows) - 1):
            row_i = rows[j]
            row_i1 = rows[j + 1]

            if row_i[2] == 1 and row_i1[2] == 1:
                if row_i[1] < row_i1[1]:
                    temp_row = rows[j]
                    rows[j] = rows[j + 1]
                    rows[j + 1] = temp_row

            if row_i[2] == 2 and row_i1[2] == 2:
                if row_i[1] > row_i1[1]:
                    temp_row = rows[j]
                    rows[j] = rows[j + 1]
                    rows[j + 1] = temp_row

            if row_i[2] == 2 and row_i1[2] == 1:
                temp_row = rows[j]
                rows[j] = rows[j + 1]
                rows[j + 1] = temp_row

        s += 1

    return rows


def make_question(model):
    model = Model.objects.get(id=model.id)
    pairs = PairsOfOptions.objects.filter(id_model=model).filter(winner_option=None)
    for pair in pairs:
        print('')
        option_1 = pair.id_option_1
        option_2 = pair.id_option_2

        path = 'api/files/models/' + model.number + '/' + pair.filename + '.txt'
        data = []

        with open(path) as f:
            lines = f.readlines()

        # Данные в файле представлены как сначала исходные данные
        # потом cтрока разделитель #####
        # потом данные которые получены в ходе выполнения опросов

        delimeter_line = 0

        n = len(lines)
        for i in range(n):
            if lines[i] == '#####':
                delimeter_line = i
                break

            else:
                l = lines[i].split(';')
                l[2] = l[2].split('\n')[0]
                data.append(l)

        if delimeter_line + 1 == n:
            # Данные не разу не сравнивались
            line_first = data[0]
            line_end = data[delimeter_line-1]

            if line_first[2] != line_end[2]:
                criteria_number = int(line_first[0])
                criteria_1 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                name_1 = criteria_1.name

                criteria_number = int(line_end[0])
                criteria_2 = Criterion.objects.filter(id_model=model).get(number=criteria_number)
                name_2 = criteria_2.name

                question = 'Преимущество по критерию: "' + name_1 + '" важнее чем преимущество по криетрию: "' \
                           + name_2 +'"'
                Message = {'question': question, 'option_1': option_1.id, 'option_2': option_2.id, 'option_1_line': 0,
                     'option_2_line': delimeter_line-1, 'model': model.id}

                return Message


def write_answer():
    pass
