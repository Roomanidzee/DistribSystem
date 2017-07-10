from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from choose_distrib.models import *
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    containers = models.ManyToManyField(Container)


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

    
def create_profile(sender, **kwargs):
    
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)    

