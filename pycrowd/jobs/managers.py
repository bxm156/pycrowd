from django.db.models import Manager


class CrowdsourceJobManager(Manager):
    
    def create_crowdsource_job(self):
        job = self.model()
        job.save(using=self._db)
        return job