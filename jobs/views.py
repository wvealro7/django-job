from django.shortcuts import render,get_object_or_404
from .models import Job
def job_list(request):
      jobs = Job.objects.all()
      context={
            'jobs': jobs,
      }
      return render(request,'jobs/jobs.html',context)

def job_detail(request,id):
      job = get_object_or_404(Job,id=id)
      return render(request,'jobs/job_details.html',{'job':job})
