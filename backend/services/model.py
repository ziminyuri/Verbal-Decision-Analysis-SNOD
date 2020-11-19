from api.models import Model
import random
from services.services import get_hash
import os


def create_model() -> object:
    try:
        model = Model.objects.create(is_demo=True)
        _create_dir(str(model.id))

        return model

    except:
        pass


def _create_dir(dir_name: str) -> None:
    path = 'api/files/models/' + dir_name

    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)