'''
Created on 13 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from .models import Laboratory, Practice, Course, ScienceHead


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