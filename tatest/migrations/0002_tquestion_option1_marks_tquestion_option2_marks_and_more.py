# Generated by Django 5.0.1 on 2024-02-02 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tquestion',
            name='option1_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='option2_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='option3_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='option4_marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tquestion',
            name='option5_marks',
            field=models.IntegerField(null=True),
        ),
    ]