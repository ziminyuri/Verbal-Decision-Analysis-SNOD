
from services.model import create_demo_model
from django.http import JsonResponse


def get_question():
    return


def registration(request):
    create_demo_model()

    return JsonResponse({"Error": "There is no city with such geonameid"})