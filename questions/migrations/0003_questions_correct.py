# Generated by Django 5.0 on 2023-12-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_remove_questions_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='correct',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
