from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Cooperator(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    
    birth_date = models.DateTimeField('дата рождения')
    
    def __str__(self):
        
        return "{0} {1}, {2}".format(self.surname, self.name, self.birth_date)
    
@receiver(post_save, sender=User)
def create_user_cooperator(self, sender, instance, created, **kwargs):
    
    if created:
        
        Cooperator.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_user_cooperator(sender, instance, **kwargs):
    instance.cooperator.save()