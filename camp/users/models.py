from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    fio = models.CharField('ФИО', max_length=255, unique=False)
    phone = PhoneNumberField('Телефон', region='RU', unique=False)
    form = models.DecimalField('Класс', max_digits=2, decimal_places=0, unique=False)

    def __str__(self):
        return f'{self.fio}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Feedback(models.Model):
    phone = PhoneNumberField('Телефон', region='RU', unique=False)

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

