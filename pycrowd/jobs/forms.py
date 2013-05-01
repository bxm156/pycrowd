
from django import forms
from pycrowd.jobs.models import CrowdsourceJob

class CrowdsourceJobForm(forms.ModelForm):
    
    class Meta:
        model = CrowdsourceJob
    