from django.db import models
from django.db.models.expressions import F

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True )

    def __str__(self):
        return self.job_name
