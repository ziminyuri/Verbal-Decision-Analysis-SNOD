from api.models import Criterion
from typing import Union


def create(model, name: str, direction: str) -> Union[object, bool]:
    try:
        if direction == 'max':
            max = True
        else:
            max = False

        criterion= Criterion.objects.create(
            id_model=model,
            name=name,
            direction=max
        )

        return criterion

    except Exception as e:
        return False