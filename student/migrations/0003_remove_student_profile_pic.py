# Generated by Django 4.2.4 on 2024-01-31 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='profile_pic',
        ),
    ]
