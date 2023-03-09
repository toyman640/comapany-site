from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


# Create your models here.

class Blog(models.Model):
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(verbose_name="Title", max_length=100)
    authur = models.CharField(verbose_name="Posted By", max_length=50)
    write_up = models.TextField(max_length=500, verbose_name="Post")

def get_image_filename(instance, filename):
    title = instance.blog.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)

class Images(models.Model):
    blog = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE, related_name='blogimages')
    image = models.ImageField(upload_to='uploads/', verbose_name="Image")


class Contact(models.Model):
    name = models.CharField(verbose_name='Name', max_length=70)
    email = models.EmailField(verbose_name='Email', max_length=50)
    subject = models.CharField(verbose_name='Subject', max_length=200)
    message = models.TextField(verbose_name='Message', max_length=500)

    def __str__(self):
        return self.name