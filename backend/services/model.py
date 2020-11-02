from api.models import Model, UserProfile
from services.criterion import create as criterion_create
from services.option import create as option_create
from services.value import create as value_create
from services.pairs_of_options import create as pairs_of_options_create


def create_demo_model() -> bool:
    # Создает демо модель для нового пользователя

    try:
        user = UserProfile.objects.get(user_id=1)
        model = Model.objects.create(is_demo=True,user=user)

        criterions: list = _create_criterions(model)
        options: list = _create_options(model)
        _set_values(criterions, options)
        _create_pairs_of_options(options)

    except Exception as e:
        return False


def _create_criterions(model) -> list:
    criterion_1 = criterion_create(model, 'Количество мест для парковки автомашин', 'max')
    criterion_2 = criterion_create(model, 'Наличие поблизости конкурентов', 'min')
    criterion_3 = criterion_create(model, 'Плотность населения в радиусе 1км (чел/кв.км)', 'max')
    criterion_4 = criterion_create(model, 'Стоимость участка (млн. долл)', 'min')
    criterion_5 = criterion_create(model, 'Поток общественного транспорта', 'max')
    criterion_6 = criterion_create(model, 'Видимость магазина с главной улицы', 'max')
    criterion_7 = criterion_create(model, 'Инфрастркутура связей', 'max')

    return [criterion_1, criterion_2, criterion_3, criterion_4, criterion_5, criterion_6, criterion_7]


def _create_options(model) -> list:
    option_1 = option_create(model, 'A1')
    option_2 = option_create(model, 'A2')
    option_3 = option_create(model, 'A3')
    option_4 = option_create(model, 'A4')

    return [option_1, option_2, option_3, option_4]


def _set_values(criterions: list, options: list) -> None:
    values = [400, 1, 200, 6, 1, 5, 3,
              300, 5, 4500, 16, 3, 5, 3,
              250, 3, 6000, 12, 5, 3, 5,
              150, 5, 7000, 20, 7, 1, 7]

    i = 0
    for option in options:
        for criterion in criterions:
            value_create(criterion, option, values[i])
            i += 1


def _create_pairs_of_options(options: list) -> None:
    n = len(options)
    m = n
    k = 1
    for i in range(n):
        for j in range(k, m):
            pairs_of_options_create(options[i], options[j])
        k += 1



