# Generated by Django 3.2.22 on 2023-10-24 09:56

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone_no', models.IntegerField(blank=True, null=True)),
                ('facebook', models.CharField(blank=True, max_length=300, null=True)),
                ('instagram', models.CharField(blank=True, max_length=300, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
