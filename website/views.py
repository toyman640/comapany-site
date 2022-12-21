from django.shortcuts import render, redirect
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        subject = 'Contact Us'
        context = {
            'name' : name,
            'email' : email,
            'date' : date,
            'time' : time,
            'message' : message
        }
        html_message = render_to_string('mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = email
        print(from_email)
        send = mail.send_mail(subject, plain_message, from_email, ['hello@skaalfarms.com', from_email], html_message=html_message)

        if send:
            messages.success(request, 'Your Message have been sent')
            return redirect('index')
        else:
            messages.error(request, 'Email not sent')
   
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):

    return render(request, 'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get['name']
        email = request.POST.get['email']
        date = request.POST.get['date']
        time = request.POST.get['time']
        message = request.POST.get['message']
        subject = 'Contact Us'
        context = {
            'name' : name,
            'email' : email,
            'date' : date,
            'time' : time,
            'message' : message
        }
        html_message = render_to_string('mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <adeyor@gmail.com>'
        send = mail.send_mail(subject, plain_message, from_email, ['info@skaalfarms.com'], html_message=html_message)

        if send:
            messages.success(request, 'Email sent successfully')
        else:
            messages.error(request, 'Email not sent')
    return render(request, 'contact.html')