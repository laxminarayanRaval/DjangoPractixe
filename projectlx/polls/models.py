from statistics import mode
from django.db import models

class Question(models.Model):
    que_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    que = models.ForeignKey(Question, on_delete=models.CASCADE)
    cho = models.CharField(max_length=200)
    vot = models.IntegerField(default=0)
