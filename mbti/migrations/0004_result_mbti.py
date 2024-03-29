# Generated by Django 5.0.1 on 2024-02-02 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbti', '0003_mquestion_course'),
        ('quiz', '0011_result_category_e_result_category_f_and_more'),
        ('student', '0004_alter_student_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result_mbti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('category_E', models.PositiveIntegerField(default=0)),
                ('category_I', models.PositiveIntegerField(default=0)),
                ('category_S', models.PositiveIntegerField(default=0)),
                ('category_N', models.PositiveIntegerField(default=0)),
                ('category_T', models.PositiveIntegerField(default=0)),
                ('category_F', models.PositiveIntegerField(default=0)),
                ('category_J', models.PositiveIntegerField(default=0)),
                ('category_P', models.PositiveIntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
