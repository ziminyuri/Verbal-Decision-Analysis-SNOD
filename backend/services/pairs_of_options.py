from api.models import PairsOfOptions


def create(options_1: object, option_2: object) -> bool:
    try:
        PairsOfOptions.objects.create(
            id_option_1=options_1,
            id_option_2=option_2,
            winner_option=None
        )
        return True

    except Exception as e:
        return False
