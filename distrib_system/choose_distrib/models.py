from django.db import models

# Create your models here.

class Lab(models.Model):   
    #лаборатория 
    lab_name = models.CharField(max_length = 100, verbose_name = 'Название лаборатории')
     
    '''
    Важный момент, в следующих полях храним ID user-ов в виде: (id_)
    For example:  213_
    Для списка (студентов например) будет выглядеть:
    123_42_7_654_23_  ...
    '''
    lab_scientific_director = models.CharField(max_length = 100, verbose_name = 'Руководитель лаборатории')
    lab_students = models.CharField(max_length = 600, verbose_name = 'Список студентов')
    lab_description = models.CharField(max_length = 1200, verbose_name = 'Описание лаборатории')
    
    def __str__(self):
        return "Название лаборатории: {0}, руководитель: {1}".format(
            self.lab_name, self.lab_scientific_director)
    
    
class Course(models.Model):
    #курс по выбору
    course_name = models.CharField(max_length = 100, verbose_name = 'Название курса')
    course_professor = models.CharField(max_length = 100, verbose_name = 'Профессор')
    course_students = models.CharField(max_length = 600, verbose_name = 'Список студентов')
    course_description = models.CharField(max_length = 1200, verbose_name = 'Описание курса')

    
    def __str__(self):
        return "Название курса: {0}, профессор: {1}".format(
            self.course_name, self.course_professor)
    
    
    '''
    Касательно практики, нужно узнать, должна ли она знать "свою" лабораторию
    Пока без
    '''
class Practice(models.Model):
    #практика
    practice_name = models.CharField(max_length = 100, verbose_name = 'Название практики')
    practice_responcible = models.CharField(max_length = 100, verbose_name = 'Куратор')
    practice_students = models.CharField(max_length = 600, verbose_name = 'Список студентов')
    practice_description = models.CharField(max_length = 1200, verbose_name = 'Описание практики')
    
    def __str__(self):
        return "Название практики: {0}, куратор: {1}".format(
            self.practice_name, self.practice_responcible)