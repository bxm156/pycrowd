
from django import forms
from pycrowd.jobs.models import CrowdsourceJob

class JobForm(forms.ModelForm):
    
    class Meta:
        model = CrowdsourceJob
    