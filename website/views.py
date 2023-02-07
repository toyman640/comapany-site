from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
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
    blog_post = Blog.objects.order_by('-date')
    return render(request, 'blog.html', {'blog_post' :blog_post})

def blog_detail(request, post_id):
    try:
        post = Blog.objects.get(id=post_id)
    except:
        pass 
    return render(request, 'detail.html')