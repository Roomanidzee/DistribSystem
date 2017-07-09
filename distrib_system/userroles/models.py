from django.db import models
from django.contrib.auth.models import User
from .fields import AutoOneToOneField   
    
class Cooperator(models.Model):
    #роль 'Сотрудник'
    work = models.CharField(max_length = 100, verbose_name = 'Специализация')
    user = AutoOneToOneField(User, related_name = 'cooperator', verbose_name=('User'), primary_key = True)

    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.work)
        
        
class Student(models.Model):
    #роль 'Студент'
    group = models.CharField(max_length = 10, verbose_name = 'Группа студента')
    user = AutoOneToOneField(User, related_name = 'student', verbose_name=('User'), primary_key = True)
    
    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.group)
        
        
class Professor(models.Model):
    #роль 'Преподаватель'
    education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
    user = AutoOneToOneField(User, related_name = 'professor', verbose_name=('User'), primary_key = True)
    
    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.education_course)


class ScientificDirector(models.Model):
    #роль 'Научный руководитель'
    education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
    user = AutoOneToOneField(User, related_name = 'scientific_director', verbose_name=('User'), primary_key = True)
    
    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.education_course)