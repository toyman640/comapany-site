# Generated by Django 4.1.2 on 2023-01-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_blog_images_delete_contactus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='blog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='blogimages', to='website.blog'),
        ),
    ]
