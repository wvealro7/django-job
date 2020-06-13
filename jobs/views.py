from django.shortcuts import render,get_object_or_404
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyModelForm


def job_list(request):
      jobs = Job.objects.all()
      paginator = Paginator(jobs, 10)
      page_number = request.GET.get('page')
      page_obj = paginator.get_page(page_number)
      context={
            'jobs': page_obj,
      }
      return render(request,'jobs/jobs.html',context)

def job_detail(request,slug):
      job = get_object_or_404(Job,slug=slug)
      if request.method == "POST":
            form = ApplyModelForm(request.POST,request.FILES)

            if form.is_valid():
                  myform = form.save(commit=False)
                  myform.job = job
                  myform.save()
                  form = ApplyModelForm()
      else:
            form = ApplyModelForm()
      
      return render(request,'jobs/job_details.html',{'job':job,'form':form})
