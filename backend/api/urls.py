from django.urls import path
from api import views

urlpatterns = [
    path('api/v1/question', views.get_question),
    path('api/v1/registration', views.registration)
]
