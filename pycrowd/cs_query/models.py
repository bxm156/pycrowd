'''
Created on Nov 6, 2012

@author: Bryan
'''
from django.db import models
from django.conf import settings
from pycrowd.cs_hits.models import HumanTask

class Question(models.Model):
    hit = models.ForeignKey(HumanTask)
    question = models.CharField(max_length=30)
    image = models.URLField()
    

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    hit = models.ForeignKey(HumanTask) # Reduce joins
    
    class Meta:
        unique_together = ('user', 'question',)

        
class Choice(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=30)


class MultipleChoiceQuestion(Question):
    correct_answer = models.ForeignKey(Choice)
    
class MultipleChoiceAnswer(Answer):
    answer = models.ForeignKey(Choice)
    

class BooleanAnswer(Answer):
    answer = models.BooleanField()  