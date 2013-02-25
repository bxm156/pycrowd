'''
Created on Nov 7, 2012

@author: Bryan
'''
from django.db import models

import pycrowd.cs_query.models
from pycrowd.cs_jobs.models import CrowdsourceJob

class HumanTaskManager(models.Manager):
    pass

class HumanTask(models.Model):
    job = models.ForeignKey(CrowdsourceJob)
    completed = models.BooleanField()
    date_finished = models.DateTimeField()
    
    objects = HumanTaskManager()
    
    class Meta:
        unique_together = (("id", "job"),)
    
    def getQuestion(self):
        return pycrowd.cs_query.models.Question.objects.get(hit=id)
    
    def getResponseCount(self):
        return pycrowd.cs_query.models.Answer.objects.filter(hit=id).count()
        