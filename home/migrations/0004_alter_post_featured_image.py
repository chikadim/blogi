# Generated by Django 3.2.22 on 2023-10-24 22:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_featured_image_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
