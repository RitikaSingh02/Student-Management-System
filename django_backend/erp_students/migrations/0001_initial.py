# Generated by Django 2.0 on 2020-06-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_NAME', models.CharField(default='NULL', max_length=250)),
                ('PASSWORD', models.CharField(default='KIET123', max_length=250)),
                ('father_name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('branch', models.CharField(max_length=250)),
                ('phone_no', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('USER_NAME', models.CharField(max_length=250)),
                ('PASSWORD', models.CharField(default='KIET123', max_length=250)),
                ('USERTYPE', models.CharField(max_length=250)),
            ],
        ),
    ]
