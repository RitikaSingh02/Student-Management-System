# Generated by Django 2.0 on 2020-06-04 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp_students', '0004_queries_new_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queries',
            name='NEW_VALUE',
        ),
        migrations.RemoveField(
            model_name='queries',
            name='query_field',
        ),
    ]
