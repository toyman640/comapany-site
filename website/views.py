from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import *
from .models import *
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail
from django.core.mail import send_mail

# Create your views here.




def index(request):
    
   
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):

    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message  = request.POST.get('message')

        form_data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message

        }
        print(message)
        html_message = render_to_string('mail-template.html', form_data)
        plain_message = strip_tags(html_message)
        from_email = 'From <hello@skaalfarms.com>'
        send = send_mail(subject, plain_message,from_email, ['info@skaalfarms.com',email], html_message=html_message, fail_silently=True)

        if send:
            messages.success(request, "Message sent successfully")
        else:
            messages.error(request, "Message not sent")

    
    return render(request, 'contact.html')

def blog(request):
    blog_post = Blog.objects.order_by('-date')
    return render(request, 'blog.html', {'blog_post' :blog_post})

def blog_detail(request, post_id):
    try:
        post = Blog.objects.get(id=post_id)
    except ObjectDoesNotExist:
        return render(request, '404.html')
        
    return render(request, 'detail.html', {'post_detail' : post})