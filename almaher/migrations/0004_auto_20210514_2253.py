# Generated by Django 3.1.7 on 2021-05-14 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almaher', '0003_course_num_of_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almaher.person'),
        ),
    ]
