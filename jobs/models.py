from django.db import models

JOB_TYPE = (
      ('FT','Full Time'),
      ('PT','Part Time'),
)

class Job(models.Model):
      title = models.CharField(max_length=150)
      #location
      job_type      = models.CharField(max_length=5, choices=JOB_TYPE)
      description   = models.TextField()
      published_at  = models.DateTimeField(auto_now=True)
      vacancy       = models.IntegerField(default=1)
      salary        = models.IntegerField(default=0)
      experience    = models.IntegerField(default=1)

      def __str__(self):
          return self.title
      
