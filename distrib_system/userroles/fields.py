'''
Created on 8 июл. 2017 г.

@author: Андрей Романов

'''
# -*- coding: utf-8 -*-

from django.db.models import OneToOneField
try:
    
   from django.db.models.fields.related import SingleRelatedObjectDescriptor
   
except ImportError:
    
   from django.db.models.fields.related_descriptors import ForwardManyToOneDescriptor as SingleRelatedObjectDescriptor

class AutoSingleRelatedObjectDescriptor(SingleRelatedObjectDescriptor):
    
    def __get__(self, instance, instance_type = None):
        
        try:
            
            return super(AutoSingleRelatedObjectDescriptor, self).__get__(instance, instance_type)             
         
        except self.related.model.DoesNotExist:
            
            obj = self.related.model(**{self.related.field.name: instance})
            obj.save()
            return obj

class AutoOneToOneField(OneToOneField):
    
    def contribute_to_related_class(self, cls, related):
        
        setattr(cls, related.get_accessor_name(), AutoSingleRelatedObjectDescriptor(related))            