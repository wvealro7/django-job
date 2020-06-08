from django.db import models

def image_upload(instance,file):
      file_name,extenion = file.split(".")

      return f"jobs/{file_name}-{instance.id}.{extenion}"

JOB_TYPE = (
      ('FT','Full Time'),
      ('PT','Part Time'),
)

class Job(models.Model):
      title = models.CharField(max_length=150)
      #location
      job_type          = models.CharField(max_length=5, choices=JOB_TYPE)
      description       = models.TextField()
      published_at      = models.DateTimeField(auto_now=True)
      vacancy           = models.IntegerField(default=1)
      salary            = models.IntegerField(default=0)
      experience        = models.IntegerField(default=1)
      category          = models.ForeignKey("Category",on_delete=models.CASCADE)
      image             = models.ImageField(upload_to=image_upload)

      def __str__(self):
          return self.title

class Category(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
          return self.name
      
