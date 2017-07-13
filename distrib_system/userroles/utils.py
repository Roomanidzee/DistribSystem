'''
Created on 12 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group, User
from .models import Student, Cooperator, Professor, ScientificDirector


def get_entity_from_db(user):
    result = []
    groups = list(user.groups.all())
    for group in groups:
        if group.name == 'student':
            result.append(Student.objects.get(user = user))
        if group.name == 'professor':
            result.append(Professor.objects.get(user = user))
        if group.name == 'cooperator':
            result.append(Cooperator.objects.get(user = user))
        if group.name == 'scientific_director':
            result.append(ScientificDirector.objects.get(user = user))
    return result


def initialize_user(user, positions):
    for p in positions:
        group, created = Group.objects.get_or_create(name=p)
        if created:
            group.save()
        user.groups.add(group)
        if p == 'student':
            st = Student(user=user)
            st.save()
        if p == 'cooperator':
            cp = Cooperator(user=user)
            cp.save()
        if p == 'professor':
            pr = Professor(user=user)
            pr.save()
        if p == 'scientific_director':
            sd = ScientificDirector(user=user)
            sd.save()
        user.save()
