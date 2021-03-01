from django.db import models
from datetime import datetime


class CallbackRequests(models.Model):
    form_type = models.CharField(name='form_type', verbose_name='Тип заявки', max_length=64)
    date_request = models.DateTimeField(name='date_request', verbose_name='Время заявки', default=datetime.now())
    name = models.CharField(name='name', verbose_name='Имя', max_length=64)
    phone = models.BigIntegerField(name='phone', verbose_name='Телефон', unique=True)
    email = models.EmailField(name='email', verbose_name='email', null=True, blank=True, unique=True)

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return str(self.email)


class ClassService(models.Model):
    name_service = models.CharField(name='name_service', verbose_name='Вид потребности', max_length=32)

    class Meta:
        verbose_name = 'Вид потребности'
        verbose_name_plural = 'Виды потребностей'

    def __str__(self):
        return str(self.name_service)


class TypeService(models.Model):
    name_service = models.CharField(name='name_service', verbose_name='Потребность', max_length=32)
    type_service = models.ForeignKey(ClassService, on_delete=models.CASCADE, verbose_name='Вид потребности')

    class Meta:
        verbose_name = 'Потребность'
        verbose_name_plural = 'Потребности'

    def __str__(self):
        return str(self.type_service)




