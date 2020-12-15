from api.models import Model, Option, Criterion, Value
import os


def create_model(demo_model: bool = False) -> object:
    try:
        if demo_model:
            model = Model.objects.create(is_demo=True, name='Демонстрационная')
        else:
            model = Model.objects.create(is_demo=True, name='Пользовательская')

        _create_dir(str(model.id))

        return model

    except:
        pass


def _create_dir(dir_name: str) -> None:
    path1 = 'api/files/models/' + dir_name
    path2 = 'media/' + dir_name

    try:
        os.mkdir(path1)
        os.mkdir(path2)
    except OSError:
        print("Создать директорию %s не удалось" % path2)


def get_model_data(model_id):
    # Возвращает данные модели из файла для отображения
    model = Model.objects.get(id=model_id)
    options = Option.objects.filter(id_model=model)

    header  = ['№','Наименование критерия']
    for option in options:
        header.append(option.name)

    data = []
    criterions = Criterion.objects.filter(id_model=model)
    for criterion in criterions:
        line = [criterion.name]
        for option in options:
            value = Value.objects.get(id_option=option, id_criterion=criterion)
            line.append(value.value)
        data.append(line)

    return data, header
