from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()    
        return redirect('/')

    context = {
            'jobs': Job.objects.all(),
            'form': JobForm()
        }

    return render(request, 'todo_app/index.html', context)

def update_job(request, job_id):
    job = Job.objects.get(id=job_id)
    form = JobForm(instance=job)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = { 
        'form': form,
        'job': job
    }
    return render(request, 'todo_app/update_job.html', context)

def delete_job(request, job_id):
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        job.delete()
        return redirect('/')
    context = {
        'job': Job.objects.get(id=job_id)
    }
    return render(request, 'todo_app/delete.html', context)



# Create your views here.
