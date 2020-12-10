import csv
import json
from datetime import datetime, timedelta

import jwt
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Criterion, Option, Value, PairsOfOptions, Model, HistoryAnswer
from services.pairs_of_options import create_files, make_question, write_answer
from services.model import create_model


JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 20


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
        model = create_model(demo_model=True)

        with open("api/files/demo.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            count = False

            criterion_number = 1
            option_number = 1
            for row in file_reader:
                if count is False:

                    for i in range(2, len(row)):
                        option = Option.objects.create(name=row[i], id_model=model, number=option_number)
                        options_obj_list.append(option)
                        option_number += 1

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

                    criterion_number += 1

                    for i in range(2, len(row)):
                        value = float(row[i])
                        Value.objects.create(value=value, id_option=options_obj_list[i-2], id_criterion=criterion)

        n = len(options_obj_list)
        k = 1
        for i in range(n):
            for j in range(k, n):
                if i != j:
                    s = PairsOfOptions.objects.create(id_option_1=options_obj_list[i], id_option_2=options_obj_list[j],
                                                      id_model=model)

            k += 1
        create_files(model)
        message = make_question(model)

        return JsonResponse(message, status=200)


@csrf_exempt
def question(request):
    if request.method == 'POST':
        json_data: dict = json.loads(request.body)
        message = write_answer(json_data)

        return JsonResponse(message, status=200)


@csrf_exempt
def get_model(request, id):
    model = Model.objects.get(id=id)
    option_shnur = Option.objects.get(id=model.id_winner_option_shnur)
    option_many = Option.objects.get(id=model.id_winner_option_many)

    # История ответов
    history_answers = HistoryAnswer.objects.filter(id_model=model)
    answers = []
    for answer_history in history_answers:
        answers.append({'question': answer_history.question, 'answer': answer_history.answer,
                        'pair': answer_history.pair.id_option_1.name + ' и ' + answer_history.pair.id_option_2.name})

    response = {'option_shnur': option_shnur.name, 'option_many': option_many.name, 'history': answers}
    return JsonResponse(response, status=200, safe=False)


@csrf_exempt
def create_model_from_csv(request):
    try:
        body = request.body

    except Exception as e:
        print(e)

    return JsonResponse('', status=200)


@csrf_exempt
def get_models(request):
    response = []
    try:
        models = Model.objects.all()

        for model in models:
            response.append({'name': model.name, 'id': model.id})

    except Exception as e:
        print(e)

    return JsonResponse(response, status=200, safe=False)
