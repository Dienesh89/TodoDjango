from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class signup(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)

    def __str__(self):
        return self.username

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.TextField()
    taskdate = models.DateField(default=datetime.date.today)
    Taskuser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "task of " + str(self.Taskuser)

