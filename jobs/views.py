from django.shortcuts import render,get_object_or_404
from .models import Job
from django.core.paginator import Paginator

def job_list(request):
      jobs = Job.objects.all()
      paginator = Paginator(jobs, 1)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      context={
            'jobs': page_obj,
      }
      return render(request,'jobs/jobs.html',context)

def job_detail(request,id):
      job = get_object_or_404(Job,id=id)
      return render(request,'jobs/job_details.html',{'job':job})
