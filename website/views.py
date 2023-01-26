from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.




def index(request):
    
   
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):

    return render(request, 'service.html')

def contact(request):
    
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_detail(request):
    return render(request, 'detail.html')