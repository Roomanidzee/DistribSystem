from django.db import models
from django.contrib.auth.models import User
    
class Cooperator(models.Model):
    #роль 'Сотрудник'
    work = models.CharField(max_length = 100, verbose_name = 'Специализация')
    user = models.ForeignKey(User, default = 1, primary_key = True)

    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.work)
        
        
class Student(models.Model):
    #роль 'Студент'
    group = models.CharField(max_length = 10, verbose_name = 'Группа студента')
    user = models.ForeignKey(User, default = 1, primary_key = True)
    
    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.group)
        
        
class Professor(models.Model):
    #роль 'Преподаватель'
    education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
    user = models.ForeignKey(User, default = 1, primary_key = True)
    
    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.education_course)


class ScientificDirector(models.Model):
    #роль 'Научный руководитель'
    education_course = models.CharField(max_length = 100, verbose_name = 'Предмет')
    user = models.ForeignKey(User, default = 1, primary_key = True)
    
    def __str__(self):
        return "{0} - {1}".format(str(self.user), self.education_course)