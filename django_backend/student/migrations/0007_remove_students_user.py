# Generated by Django 2.0 on 2020-05-26 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20200526_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='user',
        ),
    ]