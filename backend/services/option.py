from api.models import Option
from typing import Union


def create(model, name: str) -> Union[object, bool]:
    try:
        option = Option.objects.create(
            id_model=model,
            name=name,
        )

        return option

    except Exception as e:
        return False