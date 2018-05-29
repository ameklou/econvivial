from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

class Profile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name= models.CharField(max_length=250)
    birth_date=models.DateField(null=True, blank=True)
    location=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    sexe=models.CharField(max_length=2,blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    region=models.CharField(max_length=50)
    profession=models.CharField(max_length=50)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
