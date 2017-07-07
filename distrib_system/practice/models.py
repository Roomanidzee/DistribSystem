from django.db import models

# Create your models here.

class Student(models.Model):
    
    group = models.CharField(max_length = 6)
    surname = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        
        return "{0} {1}, группа: {2}".format(self.surname, self.name, self.group)