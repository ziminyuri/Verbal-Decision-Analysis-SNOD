from api.models import Model
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