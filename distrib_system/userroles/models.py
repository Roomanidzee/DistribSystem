from django.db import models
from django.contrib.auth.models import User, Group
    
class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    patronymic = models.CharField(max_length = 50, verbose_name = 'Отчество')

    def user_post_save(sender, instance, **kwargs):
        ( profile, new ) = UserProfile.objects.get_or_create(user=instance)
 
models.signals.post_save.connect(user_post_save, sender=User)     