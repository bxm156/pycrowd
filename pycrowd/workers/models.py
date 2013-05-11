'''
Created on Nov 6, 2012

@author: Bryan
'''
from django.db import models
from django.conf import settings

class WorkerProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True, editable=False)
    trust_level = models.PositiveSmallIntegerField(default=5, editable=False)
    
    