'''
Created on 12 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from .models import Student, Cooperator, Professor, ScientificDirector

def get_entity_from_db(user):
        
    result = None    
    
    if user.groups.get().name == "student":                
        result = Student.objects.get(user.id)        
    elif user.groups.get().name == "cooperator":        
        result = Cooperator.objects.get(user.id)        
    elif user.groups.get().name == "professor":        
        result = Professor.objects.get(user.id)        
    elif user.groups.get().name == "scientific_director":        
        result = ScientificDirector.objects.get(user.id)        
    else:         
        result = None
        
    return result              