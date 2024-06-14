from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Questions(models.Model):
    qno = models.CharField(max_length = 2)
    question = models.TextField()
    ans1 = models.TextField(null = True, blank = True)
    ans2 = models.TextField(null = True, blank = True)
    ans3 = models.TextField(null = True, blank = True)

    def __str__(self):
        return" Question No: "+ str(self.qno)
    

class answer(models.Model):
    ans = models.TextField(null = True, blank = True)
    class result(models.TextChoices):
        Correct = 'Correct', 'Correct'
        Wrong = 'Incorrect', 'Incorrect'
        Wait = '-', '-'
    Result = models.CharField(max_length= 10, choices = result.choices, default = result.Wait)
    qno = models.CharField(max_length = 2)
    username = models.CharField(max_length= 100)
    create = models.TimeField(datetime.time)
    points = models.IntegerField(default = 0)
    id = models.AutoField(primary_key=True,unique=True)
    def __str__(self):
        return self.username + " Question No: "+ str(self.qno)


class TotalPoints(models.Model):
    username = models.CharField(max_length= 100)
    points = models.IntegerField(default = 0)
    id = models.AutoField(primary_key=True,unique=True)
    def __str__(self):
        return self.username
    
class Messages(models.Model):
    message = models.TextField()
    username = models.CharField(max_length= 100)
    id = models.AutoField(primary_key=True,unique=True)
    def __str__(self):
        return self.username