'''
Created on 13 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-
import importlib

from .models import Request, StudentToLabStorage



modulename, dot, classname = 'choose_distrib.models.classname'.rpartition('.')
module = importlib.import_module(modulename)

class Pair:
    def __init__(self, first_item, second_item):
        self.list = []
        self.first_item = first_item
        self.second_item = second_item


# Автор следующих четырех функций: Роман
def get_container_with_number_of_occupied_from_db(user ,container_type):
    containers = list(getattr(module, container_type).objects.all())
    list_of_pairs = []
    for container in containers:
        temp = StudentToLabStorage.objects.filter(container=container).distinct().count()
        pair = Pair(container, temp)
        list_of_pairs.append(pair)

    return list_of_pairs

# Автор следующих четырех функций: Андрей
def get_containers_from_db(user, container_class):
    containers = getattr(module, container_class).objects.all()
    return list(containers)
    
def get_requests_for_student(user, request_type):
    requests=list(Request.objects.filter(request_type=request_type, student=user))
    return requests
    
    
    
    
    
    
    
