from api.models import Model, Criterion, PairsOfOptions, Value, Option


def create_files(model: object):
    model = Model.objects.get(id=model.id)
    pairs = PairsOfOptions.objects.filter(id_model=model)

    rows = []
    for i in pairs:
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

        s = 1
        for k in range(len(rows)-s):
            for i in range(len(rows)-1):
                row_i = rows[i]
                row_i1 = rows[i+1]

                if row_i[2] == 1 and row_i1[2] == 1:
                    if row_i[1] < row_i1[1]:
                        temp_row = rows[i]
                        rows[i]= rows[i+1]
                        rows[i+1] = temp_row

                if row_i[2] == 2 and row_i1[2] == 2:
                    if row_i[1] > row_i1[1]:
                        temp_row = rows[i]
                        rows[i]= rows[i+1]
                        rows[i+1] = temp_row

                if row_i[2] == 2 and row_i1[2] == 1:
                    temp_row = rows[i]
                    rows[i] = rows[i + 1]
                    rows[i + 1] = temp_row

            s +=1

        print('fds')



def _precent(value, max) -> float:
    return value / (max / 100)