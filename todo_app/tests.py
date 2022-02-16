from django.test import TestCase
from .models import *

class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_job(self):
        job = Job()
        job.job_name = "I am a test."
        job.done = False
        job.save()
        record = Job.objects.get(pk=1)
        self.assertEqual(record, job)