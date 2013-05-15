
from django import forms
from pycrowd.jobs.models import CrowdsourceJob

class CrowdsourceJobForm(forms.ModelForm):
    
    class Meta:
        model = CrowdsourceJob
        
    def save(self):
        return self.Meta.model.objects.create_crowdsource_job(self.cleaned_data)
    