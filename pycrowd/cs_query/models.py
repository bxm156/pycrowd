'''
Created on Nov 6, 2012

@author: Bryan
'''
from django.db import models
from django.conf import settings
import pycrowd.cs_hits.models

class Question(models.Model):
    hit = models.ForeignKey(pycrowd.cs_hits.models.HumanTask)
    question = models.CharField(max_length=30)
    image = models.URLField()
    

class Answer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey(Question)
    
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