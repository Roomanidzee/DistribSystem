from django.db import models
from django.contrib.auth.models import User
from .fields import AutoOneToOneField   
 
class AbstractPerson(models.Model):
    surname = models.CharField(max_length = 100, verbose_name = 'Фамилия')
    name = models.CharField(max_length = 100, verbose_name = 'Имя')
    patronymic = models.CharField(max_length = 100, verbose_name = 'Отчество')
    email = models.EmailField(max_length = 50, verbose_name = 'Почта')
    password = models.CharField(max_length = 16, verbose_name = 'Пароль')
    
    
class Cooperator(AbstractPerson):
    #роль 'Сотрудник'
    work = models.CharField(max_length = 50, verbose_name = 'Специализация')

    def __str__(self):
        return "{0} {1} {2}, login: {3}, password: {4}, work: {5}".format(
            self.surname, self.name, self.patronymic, self.email, self.password, self.work)
        
        
class Student(AbstractPerson):
    #роль 'Студент'
    group = models.CharField(max_length = 10, verbose_name = 'Группа студента')
    course = models.CharField(max_length = 10, verbose_name = 'Курс студента')
    
    def __str__(self):
        return "{0} {1} {2}, login: {3}, password: {4}, group: {5}, course: {6}".format(
            self.surname, self.name, self.patronymic, self.email, self.password, self.group, self.course)
        

class Professor(AbstractPerson):
	#роль 'Преподаватель'
	education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
	
	def __str__(self):
		return "{0} {1} {2}, login: {3}, password: {4}, education_course: {5}".format(
			self.surname, self.name, self.patronymic, self.email, self.password, self.education_course)

class ScientificDirector(AbstractPerson):
	#роль 'Научный руководитель'
	education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
	
	def __str__(self):
		return "{0} {1} {2}, login: {3}, password: {4}, education_course: {5}".format(
			self.surname, self.name, self.patronymic, self.email, self.password, self.education_course)
	     
class Profile(models.Model):
    user = AutoOneToOneField(User, related_name = 'profile', verbose_name=('User'), primary_key = True)
    cooperator = models.ForeignKey(Cooperator, verbose_name = 'Сотрудник', null = True)     
    student = models.ForeignKey(Student, verbose_name = 'Студент', null = True)
    professor = models.ForeignKey(Professor, verbose_name = 'Преподаватель', null = True)
    scientific_director = models.ForeignKey(ScientificDirector, verbose_name = 'Научный руководитель', null = True)

    def __str__(self):
        
        return "Cooperator : {0}\n, Student: {1}\n, Professor: {2}\n, ScientificDirector: {3}\n".format(
            str(self.cooperator), str(self.student), str(self.professor), str(self.scientific_director))
    
