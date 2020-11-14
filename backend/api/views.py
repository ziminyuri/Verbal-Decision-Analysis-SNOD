from services.model import create_demo_model
from django.contrib import auth
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.models import User
import jwt

from datetime import datetime, timedelta
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20


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

            if user:
                payload = {
                    'user_id': user.id,
                    'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
                }
                jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
                return JsonResponse({"token": jwt_token.decode('utf-8'),'user_id': user.id}, status=200)

            return JsonResponse({'Message': 'Пользователя не существует'}, status=400)

        except Exception as e:
            return JsonResponse({"Message": "Ошибка при авторизации пользователя"}, status=400)



