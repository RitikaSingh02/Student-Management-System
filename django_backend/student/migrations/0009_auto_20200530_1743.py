# Generated by Django 2.0 on 2020-05-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200530_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='students',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]