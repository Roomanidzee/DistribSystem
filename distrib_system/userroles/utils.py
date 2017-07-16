'''
Created on 12 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from django.contrib.auth.models import Group, User
from .models import Student, Cooperator, Professor, ScientificDirector
import importlib

modulename, dot, classname = 'userroles.models.classname'.rpartition('.')
module = importlib.import_module(modulename)

# Возвращает ассоц. массив
def get_entity_from_db(user, name):
    model = None
    try :
        model=getattr(module, name).objects.get(user=user)
        if model is not None:
            return model
    except:
        return None


def initialize_user(user, positions):
    for p in positions:
        model = getattr(module, p)(user=user)
        model.save()