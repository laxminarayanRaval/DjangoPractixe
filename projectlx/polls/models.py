import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin  # for display decorator

class Question(models.Model):
    que_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.que_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published Recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
