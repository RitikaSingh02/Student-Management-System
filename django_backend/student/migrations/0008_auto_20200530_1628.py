# Generated by Django 2.0 on 2020-05-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_students_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone_no',
            field=models.BigIntegerField(unique=True),
        ),
    ]
