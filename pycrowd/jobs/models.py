'''
Created on Nov 6, 2012

@author: Bryan
'''
from django.db import models
from django.conf import settings

from pycrowd.jobs.managers import CrowdsourceJobManager

class CrowdsourceJob(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    instructions = models.TextField()
    target_accuracy = models.PositiveIntegerField()
    task_count = models.IntegerField(editable=False)
    
    objects = CrowdsourceJobManager()