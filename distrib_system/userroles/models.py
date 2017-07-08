from django.db import models
from django.contrib.auth.models import User
from .fields import AutoOneToOneField    
    
class Cooperator(models.Model):
    
    #роль 'Сотрудник'
    surname = models.CharField(max_length = 100, verbose_name = 'Фамилия')
    name = models.CharField(max_length = 100, verbose_name = 'Имя')
    patronymic = models.CharField(max_length = 100, verbose_name = 'Отчество')
    email = models.CharField(max_length = 50, verbose_name = 'Почта')
    password = models.CharField(max_length = 16, verbose_name = 'Пароль')
    work = models.CharField(max_length = 50, verbose_name = 'Специализация')
    
class Profile(models.Model):
    
    user = AutoOneToOneField(User, related_name = 'profile', verbose_name=('User'), primary_key = True)
    cooperator = models.ForeignKey(Cooperator, verbose_name = 'Сотрудник')     