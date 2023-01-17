from django.db import models
from django.utils import timezone
import random
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
import string

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', blank=True, null=True)
    email = models.EmailField()
    date = models.DateField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.surname


class SubscripedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    conf_digit = models.CharField(max_length=20)
    confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class HouseType(models.Model):
    name = models.CharField(max_length=50, verbose_name='House Type')

    def __str__(self):
        return self.name


class Property(models.Model):
    date = models.DateField(timezone.now)
    title =models.CharField(max_length=100, verbose_name='Title')
    house_type = models.ForeignKey(HouseType, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='price')
    rooms = models.IntegerField(verbose_name='Rooms')
    toilet = models.IntegerField(verbose_name='Toilet')
    Bathroom = models.IntegerField(verbose_name='Bathroom')
    description = models.TextField(verbose_name='Description')
    image1 = models.ImageField(null=True, blank=True, verbose_name='Image 1', upload_to='uploads/')
    image2 = models.ImageField(null=True, blank=True, verbose_name='Image 1', upload_to='uploads/')
    image3 = models.ImageField(null=True, blank=True, verbose_name='Image 1', upload_to='uploads/')
    image4 = models.ImageField(null=True, blank=True, verbose_name='Image 1', upload_to='uploads/')
    slug = models.SlugField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural = 'Property'

    def image_1(self):
        if self.image1:
            return self.image1.url


def random_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug  = slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_generator(size= 10))
        return unique_slug_generator(instance, new_slug= new_slug)
    return slug

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender= Property)