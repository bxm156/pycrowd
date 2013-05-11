from django import forms
from django.db.models.loading import get_model
from pycrowd import settings

class WorkerForm(forms.ModelForm):

    class Meta:
        model = get_model(*settings.WORKER_PROFILE.split('.',1))