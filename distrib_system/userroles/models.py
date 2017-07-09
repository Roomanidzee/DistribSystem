from django.db import models
from django.contrib.auth.models import User
from .fields import AutoOneToOneField   
 
class AbstractPerson(models.Model):
    surname = models.CharField(max_length = 100, verbose_name = 'Фамилия')
    name = models.CharField(max_length = 100, verbose_name = 'Имя')
    patronymic = models.CharField(max_length = 100, verbose_name = 'Отчество')
    
    
class Cooperator(AbstractPerson):
    #роль 'Сотрудник'
    work = models.CharField(max_length = 50, verbose_name = 'Специализация')
    user = AutoOneToOneField(User, related_name = 'cooperator', verbose_name=('User'), primary_key = True)

    def __str__(self):
        return "{0} {1} {2}, work: {3}".format(
            self.surname, self.name, self.patronymic, self.work)
        
        
class Student(AbstractPerson):
    #роль 'Студент'
    group = models.CharField(max_length = 10, verbose_name = 'Группа студента')
    course = models.CharField(max_length = 10, verbose_name = 'Курс студента')
    user = AutoOneToOneField(User, related_name = 'student', verbose_name=('User'), primary_key = True)
    
    def __str__(self):
        return "{0} {1} {2}, group: {3}, course: {4}".format(
            self.surname, self.name, self.patronymic, self.group, self.course)
        

class Professor(AbstractPerson):
    #роль 'Преподаватель'
    education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
    user = AutoOneToOneField(User, related_name = 'professor', verbose_name=('User'), primary_key = True)
    
    def __str__(self):
        return "{0} {1} {2}, education_course: {3}".format(
			self.surname, self.name, self.patronymic, self.education_course)

class ScientificDirector(AbstractPerson):
    #роль 'Научный руководитель'
    education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
    user = AutoOneToOneField(User, related_name = 'scientific_director', verbose_name=('User'), primary_key = True)

    def __str__(self):
        return "{0} {1} {2}, education_course: {3}".format(
            self.surname, self.name, self.patronymic, self.education_course)
             
class Profile(models.Model):
    user = AutoOneToOneField(User, related_name = 'profile', verbose_name=('User'), primary_key = True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        
        return "Bio : {0}\n, location: {1}, birth date: {2}".format(
            self.bio, self.location, self.birth_date)
    
