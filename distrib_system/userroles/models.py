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
    
    def __str__(self):
        
        return "{0} {1} {2}, login: {3}, password : {4}, work : {5}".format(
            self.surname, self.name, self.patronymic, self.email, self.password, self.work)
    
class Cooperator(AbstractPerson):
    
    #роль 'Сотрудник'
   
class Professor(AbstractPerson):
	
	#роль 'Преподаватель'
	education_course = CharField(max_length = 100, verbose_name = 'Предмет')
	is_lecturer = BooleanField(verbose_name = 'Лектор')
	is_practician = BooleanField(verbose_name = 'Преподаватель практики')

class ScientificDirector(AbstractPerson):
	
	#роль 'Научный руководитель'
	education_course = CharField(max_length = 100, verbose_name = 'Предмет')
	
class Profile(models.Model):
    
    user = AutoOneToOneField(User, related_name = 'profile', verbose_name=('User'), primary_key = True)
    cooperator = models.ForeignKey(Cooperator, verbose_name = 'Сотрудник') 
	professor = models.ForeignKey(Professor, verbose_name = 'Преподаватель')
	scientific_director = models.ForeignKey(ScientificDirector, verbose_name = 'Научный руководитель')