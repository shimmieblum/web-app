import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Create your models here.

'''
Each class is a model, the variables in a classs are the db fields for that model
'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    urgency = models.IntegerField(default=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
    def __str__(self) -> str:
        return self.question_text
    
    def recently_published(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    name = models.CharField(default='john smith', max_length=40)
    
    
    def __str__(self) -> str:
        return self.choice_text
    