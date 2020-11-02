from api.models import Value


def create(criterion, option, value) -> bool:
    try:
        Value.objects.create(
            value=value,
            id_criterion=criterion,
            id_option=option
        )

        return True

    except Exception as e:
        return False