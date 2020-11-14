from services.model import create_demo_model
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.models import User


@csrf_exempt  # to make true read https://stackoverflow.com/questions/17716624/django-csrf-cookie-not-set
def registration(request):
    # create_demo_model()
    if request.method == 'POST':
        json_data: dict = json.loads(request.body)

        try:
            email: str = json_data["email"]
            password: str = json_data["password"]
            User.objects.create_user(email, email, password)
            return JsonResponse({"Message": "Пользователь создан"})

        except Exception as e:
            return JsonResponse({"Message": "Ошибка при создании пользователя"})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data: dict = json.loads(request.body)

        try:
            email: str = json_data["email"]
            password: str = json_data["password"]
            user = auth.authenticate(username=email, password=password)
            return JsonResponse({"Message": "Авторизовались"})

        except Exception as e:
            return JsonResponse({"Message": "Ошибка при авторизации пользователя"})

def get_question():
    return


