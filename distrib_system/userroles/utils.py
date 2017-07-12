'''
Created on 12 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from .models import Student, Cooperator, Professor, ScientificDirector


def get_entity_from_db(user):

    result = None

    if user.groups.get().name == "student":                
        result.append(Student.objects.get(user.id))
    if user.groups.get().name == "cooperator":
        result.append(Cooperator.objects.get(user.id))
    if user.groups.get().name == "professor":
        result.append(Professor.objects.get(user.id))
    if user.groups.get().name == "scientific_director":
        result.append(ScientificDirector.objects.get(user.id))

    return result
