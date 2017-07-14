'''
Created on 13 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from .models import Laboratory, StudentToLabStorage, Practice, Course, ScienceHead


# Автор следующих четырех функци1: Андрей
def get_practice_from_db(user):
    
    practices = Practice.objects.all()
    
    """
    
    result = []
    
    for practice_item in practices:
        
        if practice_item.pk == student.pk:
            
            result.append(practice_item)
            
    """        
    
    return list(practices)

def get_course_from_db(user):
    
    student = StudentToLabStorage.objects.get(student = user)
    
    courses = Course.objects.all()
    
    result = []
    
    for course_item in courses:
        
        if course_item.pk == student.pk:
            
            result.append(course_item)
            
    return result  

def get_lab_from_db(user):
    
    student = StudentToLabStorage.objects.get(student = user) 
    
    labs = Laboratory.objects.all() 
    
    result = []
    
    for lab_item in labs:
        
        if lab_item.pk == student.pk:
            
            result.append(lab_item)
            
    return result

def get_scidir_from_db(user):
    
    student = StudentToLabStorage.objects.get(student = user)
    
    sci_dirs = ScienceHead.objects.all()
    
    result = []
    
    for scidir_item in sci_dirs:
        
        if scidir_item.pk == student.pk:
            
            result.append(scidir_item)
            
    return result               