from django.conf import settings as django_settings
from pycrowd import defaults as pycrowd_settings

class SettingsHandler(object):
    def __getattr__(self, name):
        return getattr(django_settings, name, getattr(pycrowd_settings, name))
    
settings = SettingsHandler()
