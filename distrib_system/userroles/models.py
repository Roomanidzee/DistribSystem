from django.db import models
from django.contrib.auth.models import User, Group
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    patronymic = models.CharField(max_length = 50, verbose_name = 'Отчество')

    #def user_post_save(self, sender, instance, **kwargs):
    #    ( profile, new ) = UserProfile.objects.get_or_create(user=instance)
 
#models.signals.post_save.connect(UserProfile.user_post_save, sender=User)  

class StudentManager(models.Manager):

    def get_query_set(self):
        return super(StudentManager, self).get_query_set().filter(student__enrolled=True).distinct()

class Student(Group):
    group = models.CharField(max_length = 10)
    objects = models.Manager()
    has_students = StudentManager()
    
    class Meta:
        verbose_name_plural = "Students"
        ordering = ['name']
        permissions = {}
   
class CooperatorManager(models.Manager):

    def get_query_set(self):
        return super(CooperatorManager, self).get_query_set().filter(cooperator__enrolled=True).distinct()

class Cooperator(Group):
    work = models.CharField(max_length = 100)
    objects = models.Manager()
    has_students = CooperatorManager()
    
    class Meta:
        verbose_name_plural = "Cooperators"
        ordering = ['name']
        permissions = {}
   
class ProfessorManager(models.Manager):

    def get_query_set(self):
        return super(ProfessorManager, self).get_query_set().filter(professor__enrolled=True).distinct()

class Professor(Group):
    education_course = models.CharField(max_length = 100)
    objects = models.Manager()
    has_students = ProfessorManager()
    
    class Meta:
        verbose_name_plural = "Professors"
        ordering = ['name']
        permissions = {}

class ScientificDirectorManager(models.Manager):

    def get_query_set(self):
        return super(ScientificDirectorManager, self).get_query_set().filter(scientificdirector__enrolled=True).distinct()
        
class ScientificDirector(Group):
    education_course = models.CharField(max_length = 100)
    objects = models.Manager()
    has_students = ScientificDirectorManager()
    
    class Meta:
        verbose_name_plural = "Scientific directors"
        ordering = ['name']
        permissions = {}
   