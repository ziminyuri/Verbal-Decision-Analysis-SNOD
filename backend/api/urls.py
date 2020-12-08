from django.urls import path

from api import views

urlpatterns = [
    path('api/v1/registration', views.registration),
    path('api/v1/login', views.login),
    path('api/v1/model/demo/create', views.demo_create),
    path('api/v1/question', views.question),
    path('api/v1/model/result/<int:id>', views.get_model)
]
