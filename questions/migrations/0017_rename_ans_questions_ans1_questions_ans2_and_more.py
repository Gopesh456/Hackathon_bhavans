# Generated by Django 5.0 on 2024-06-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_messages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='ans',
            new_name='ans1',
        ),
        migrations.AddField(
            model_name='questions',
            name='ans2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='ans3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
