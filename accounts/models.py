from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile/')
    city = models.ForeignKey("City", related_name='user_city', on_delete=models.DO_NOTHING,blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
@receiver(post_save, sender=User)
def profile_post_save_receiver(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
