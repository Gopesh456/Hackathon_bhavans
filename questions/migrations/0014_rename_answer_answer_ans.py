# Generated by Django 5.0.6 on 2024-05-18 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_rename_ans_answer_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='ans',
        ),
    ]
