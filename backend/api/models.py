from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    # Модель пользователя расширяет стандартную модель пользователя Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.first_name


class Model(models.Model):
    # Модель
    is_demo = models.BooleanField()
    name = models.CharField(max_length=255)
    # Так делать не нужно
    id_winner_option_shnur = models.IntegerField(null=True)    # id победителя по методу ШНУР
    id_winner_option_many = models.IntegerField(null=True)      # id победителя по многокриетриальному методу


class Criterion(models.Model):
    # Модель критерием
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    direction = models.BooleanField()     # max (True) or min (False)
    id_model = models.ForeignKey(Model, on_delete=models.CASCADE)
    max = models.FloatField()

    def __str__(self):
        return self.name


class Option(models.Model):
    # Модель вариантов
    name = models.CharField(max_length=200)
    id_model = models.ForeignKey(Model, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class Value(models.Model):
    # Значение варианта у критерия
    value = models.FloatField()
    id_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    id_criterion = models.ForeignKey(Criterion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.value)


class PairsOfOptions(models.Model):
    # Пары вариантов и результаты их сравнения
    id_option_1 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='id_option_1')
    id_option_2 = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='id_option_2')
    winner_option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='winner_option', blank=True,
                                      null=True)
    winner_option_many = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='winner_option_many', blank=True,
                                      null=True)
    id_model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
       return str(self.id_option_1) + '' + str(self.id_option_2)
