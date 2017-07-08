from django.db import models
from django.contrib.auth.models import User
from .fields import AutoOneToOneField   
 
class AbstractPerson(models.Model):
    surname = models.CharField(max_length = 100, verbose_name = 'Фамилия')
    name = models.CharField(max_length = 100, verbose_name = 'Имя')
    patronymic = models.CharField(max_length = 100, verbose_name = 'Отчество')
    email = models.EmailField(max_length = 50, verbose_name = 'Почта')
    password = models.CharField(max_length = 16, verbose_name = 'Пароль')
    work = models.CharField(max_length = 50, verbose_name = 'Специализация')
    
    
class Cooperator(AbstractPerson):
    #роль 'Сотрудник'
    
    def __str__(self):
        
        return "{0} {1} {2}, login: {3}, password : {4}, work : {5}".format(
            self.surname, self.name, self.patronymic, self.email, self.password, self.work)
        
        
class Student(AbstractPerson):
    #роль 'Студент'
    group = models.CharField(max_length = 20, verbose_name = 'Группа студента')
    course = models.CharField(max_length = 20, verbose_name = 'Курс студента')
    def __str__(self):
        
        return "{0} {1} {2}, login: {3}, password : {4}, work : {5}".format(
            self.surname, self.name, self.patronymic, self.email, self.password, self.work)
        
        
class Profile(models.Model):
    
    user = AutoOneToOneField(User, related_name = 'profile', verbose_name=('User'), primary_key = True)
    cooperator = models.ForeignKey(Cooperator, verbose_name = 'Сотрудник')     
    student = models.ForeignKey(Student, verbose_name = 'Студент')
    