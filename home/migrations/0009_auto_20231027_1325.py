# Generated by Django 3.2.22 on 2023-10-27 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20231027_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectCategory',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='selectcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.selectcategory'),
        ),
    ]
