# Generated by Django 5.0.6 on 2024-06-01 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_totalpoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('message', models.TextField()),
                ('username', models.CharField(max_length=100)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]