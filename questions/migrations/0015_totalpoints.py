# Generated by Django 5.0.6 on 2024-05-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_rename_answer_answer_ans'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalPoints',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]