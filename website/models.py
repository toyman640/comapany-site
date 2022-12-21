from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', blank=True, null=True)
    email = models.EmailField()
    date = models.DateField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.surname