# Generated by Django 5.0 on 2023-12-25 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_alter_answer_correct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='correct',
            new_name='Result',
        ),
    ]