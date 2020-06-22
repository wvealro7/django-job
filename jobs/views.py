from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import ApplyModelForm, JobForm
from .models import Job


def job_list(request):
    ''' Get List Jobs From Database '''
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj,
    }
    return render(request, 'jobs/jobs.html', context)


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    if request.method == "POST":
        form = ApplyModelForm(request.POST, request.FILES)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
            form = ApplyModelForm()
    else:
        form = ApplyModelForm()

    return render(request, 'jobs/job_details.html', {'job': job, 'form': form})

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('jobs:list'))

    else:
        form = JobForm()
    context ={
    'form': form
    }
    return render(request, 'jobs/form.html', context)

