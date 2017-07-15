'''
Created on 13 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from .models import Laboratory, Practice, Course, ScienceHead,\
                    StudentToLabStorage, Request

#Автор следующих четырех функций: Андрей

def get_practice_requests(user):    
    practice_requests = Request.objects.filter(request_type = 'PRACTICE').filter(container = user.student)
    
    return practice_requests

def get_course_requests(user):    
    course_requests = Request.objects.filter(request_type = 'COURSE').filter(container = user.student)
    
    return course_requests

def get_lab_requests(user):    
    lab_requests = Request.objects.filter(request_type = 'LAB').filter(container = user.student)
    
    return lab_requests

def get_scidir_requests(user):    
    scidir_requests = Request.objects.filter(request_type = 'SCIENCE_HEAD').filter(container = user.student)
    
    return scidir_requests

class Pair:
    def __init__(self, first_item, second_item):
        self.list = []
        self.first_item = first_item
        self.second_item = second_item


# Автор следующих четырех функций и верхнего класса: Роман
def get_practice_with_number_of_occupied_from_db(user):
    practices = Practice.objects.all()

    list_of_pairs = []
    for practice in practices:
        temp = StudentToLabStorage.objects.filter(container=practice).distinct().count()
        pair = Pair(practice, temp)
        list_of_pairs.append(pair)

    return list_of_pairs


def get_course_with_number_of_occupied_from_db(user):
    courses = Course.objects.all()

    list_of_pairs = []
    for course in courses:
        temp = StudentToLabStorage.objects.filter(container=course).distinct().count()
        pair = Pair(course, temp)
        list_of_pairs.append(pair)

    return list_of_pairs


def get_lab_with_number_of_occupied_from_db(user):
    labs = Laboratory.objects.all()

    list_of_pairs = []
    for lab in labs:
        temp = StudentToLabStorage.objects.filter(container=lab).distinct().count()
        pair = Pair(lab, temp)
        list_of_pairs.append(pair)

    return list_of_pairs


def get_sci_dir_with_number_of_occupied_from_db(user):
    dirs = ScienceHead.objects.all()

    list_of_pairs = []
    for sci_dir in dirs:
        temp = StudentToLabStorage.objects.filter(container=sci_dir).distinct().count()
        pair = Pair(sci_dir, temp)
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