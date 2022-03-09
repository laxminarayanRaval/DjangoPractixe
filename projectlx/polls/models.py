import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    que_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    ans_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.que_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def is_answer(self, answer):
        return self.ans_text == answer

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote_text = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
