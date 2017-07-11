from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User)
    group = models.CharField(max_length=10, blank=True)
    course = models.CharField(max_length=20, blank=True)


class Cooperator(models.Model):
    user = models.OneToOneField(User)
    work = models.CharField(max_length=100, blank=True)


class Professor(models.Model):
    user = models.OneToOneField(User)
    education_course = models.CharField(max_length=100, blank=True)


class ScientificDirector(models.Model):
    user = models.OneToOneField(User)
    education_course = models.CharField(max_length=100, blank=True)
