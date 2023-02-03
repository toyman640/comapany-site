from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Name')
    surname = models.CharField(max_length=50, verbose_name='Surname')
    email = models.EmailField(verbose_name='Email')

    def __str__(self):
        return self.name