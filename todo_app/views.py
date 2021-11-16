from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):

    context = {
        'jobs': Job.objects.all(),
        'form': JobForm()
    }
    return render(request, 'todo_app/index.html', context)

# Create your views here.
