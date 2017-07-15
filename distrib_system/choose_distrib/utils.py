'''
Created on 13 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-
import importlib

from .models import Laboratory, Practice, Course, ScienceHead, StudentToLabStorage


modulename, dot, classname = 'choose_distrib.models.classname'.rpartition('.')
module = importlib.import_module(modulename)


class Pair:
    def __init__(self, first_item, second_item):
        self.list = []
        self.first_item = first_item
        self.second_item = second_item


# list(getattr(module, request_type).objects.all())
def get_container_with_number_of_occupied_from_db(user, imp_module, request_type):

    containers = list(getattr(imp_module, request_type).objects.all())
    list_of_pairs = []
    for container in containers:
        temp = StudentToLabStorage.objects.filter(container=container).distinct().count()
        pair = Pair(container, temp)
        list_of_pairs.append(pair)

    return list_of_pairs


# Автор следующих четырех функций: Андрей
def get_practice_from_db(user):
    practices = Practice.objects.all()
    return list(practices)


def get_course_from_db(user):
    courses = Course.objects.all()
    return list(courses)  


def get_lab_from_db(user):
    labs = Laboratory.objects.all() 
    return list(labs)


def get_scidir_from_db(user):
    sci_dirs = ScienceHead.objects.all()
    return list(sci_dirs)               