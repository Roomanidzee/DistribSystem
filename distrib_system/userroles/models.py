from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    
def create_profile(sender, **kwargs):
    
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)    