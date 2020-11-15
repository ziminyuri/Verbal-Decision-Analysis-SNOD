import csv
import json
import random
from datetime import datetime, timedelta

import jwt
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Criterion, Model, Option, Value, PairsOfOptions
from services.pairs_of_options import create_files

import hashlib

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20

# Функция получения хеша
def get_hash(password):
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    password_hash = hash.hexdigest()
    return password_hash

@csrf_exempt  # to make true read https://stackoverflow.com/questions/17716624/django-csrf-cookie-not-set
def registration(request):
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

            return JsonResponse({"Message": "Пользователя не существует"}, status=400)

        except Exception as e:
            return JsonResponse({"Message": "Ошибка при авторизации пользователя"}, status=400)



def demo_create(request):
    if request.method == 'GET':
        options_obj_list = []
        number_rundom: str = str(random.random())
        number_rundom = get_hash(number_rundom)

        model = Model.objects.create(is_demo=True, number=number_rundom)
        with open("api/files/demo.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = False

            criterion_number = 1
            option_number = 1
            for row in file_reader:
                if count == False:

                    for i in range(2, len(row)):
                        s = row[i]
                        option = Option.objects.create(name=row[i], id_model=model, number=option_number)
                        options_obj_list.append(option)
                        option_number +=1

                    count = True

                else:

                    if row[1] == 'min':
                        direction = False
                    else:
                        direction = True

                    max = float(row[2])
                    for i in range(3, len(row)):
                        if max < float(row[i]):
                            max = float(row[i])

                    criterion = Criterion.objects.create(name=row[0], id_model=model, direction=direction, max=max,
                                                         number=criterion_number)

                    criterion_number+=1

                    for i in range(2, len(row)):
                        value = float(row[i])
                        Value.objects.create(value=value, id_option=options_obj_list[i-2], id_criterion=criterion)

        n = len(options_obj_list)
        k=1
        for i in range(n):
            for j in range(k, n):
                if i != j:
                    number_rundom: str = str(random.random())
                    number_rundom = get_hash(number_rundom)

                    s = PairsOfOptions.objects.create(id_option_1=options_obj_list[i], id_option_2=options_obj_list[j],
                                                      id_model=model, filename=number_rundom)


            k+=1
        create_files(model)
        return JsonResponse({"Message": ""},status=200)

