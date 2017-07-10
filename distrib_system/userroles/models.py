from django.db import models
from django.contrib.auth.models import User, Group
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    timezone = models.CharField(max_length = 50, default = 'UTC')