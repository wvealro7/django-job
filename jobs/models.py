from django.db import models
from django.utils.text import slugify
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
      slug              = models.SlugField(allow_unicode=True,blank=True,null=True)

      def __str__(self):
          return self.title
      
      def save(self, *args,**kwargs):
            self.slug = slugify(self.title,allow_unicode=True)
            super(Job,self).save(*args,**kwargs)

class Category(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
          return self.name


class Applay(models.Model):
      name              = models.CharField(max_length=50)
      email             = models.EmailField(max_length=254)
      website           = models.URLField(max_length=200)
      cv                = models.FileField(upload_to='apply')
      cover_letter      = models.TextField()
      job               = models.ForeignKey(Job, on_delete=models.CASCADE,related_name='apply_job')
      created_at        = models.DateTimeField(auto_now=True)
      
      def __str__(self):
          return self.name

      
      
      
