from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Questions(models.Model):
    qno = models.CharField(max_length = 2)
    question = models.TextField()
    ans = models.TextField(null = True, blank = True)

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
    id = models.AutoField(primary_key=True,unique=True)
    def __str__(self):
        return self.username + " Question No: "+ str(self.qno)
