# Generated by Django 4.2.4 on 2024-02-02 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_result_category_e_result_category_f_and_more'),
        ('tatest', '0003_alter_tquestion_option1_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tquestion',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.course'),
        ),
    ]
