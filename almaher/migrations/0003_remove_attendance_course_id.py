# Generated by Django 3.1.7 on 2021-04-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almaher', '0002_auto_20210408_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='course_id',
        ),
    ]
