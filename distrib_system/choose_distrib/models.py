from django.db import models
from ..userroles.models import UserProfile

# Create your models here.

class Lab(models.Model):   
    #лаборатория 
    lab_name = models.CharField(max_length = 100, verbose_name = 'Название лаборатории')
    
    user = models.ForeignKey(UserProfile)
    lab_director = models.OneToOneField(UserProfile)
    
    
    def __str__(self):
        return "Название лаборатории: {0}".format(self.lab_name)
    
    
class Course(models.Model):
    #курс по выбору
    course_name = models.CharField(max_length = 100, verbose_name = 'Название курса')

    user = models.ForeignKey(UserProfile)
    course_professor = models.OneToOneField(UserProfile)
    
    def __str__(self):
        return "Название курса: {0}, профессор: {1}".format(self.course_name)
    
   
class Practice(models.Model):
    #практика
    practice_name = models.CharField(max_length = 100, verbose_name = 'Название практики')
    
    user = models.ForeignKey(UserProfile)
    practice_responsible = models.OneToOneField(UserProfile)
    
    def __str__(self):
        return "Название практики: {0}".format(self.practice_name)