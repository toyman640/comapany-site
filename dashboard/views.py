from django.shortcuts import render, redirect, get_list_or_404
from django.forms import modelformset_factory
from website.forms import *
from website.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Email or password incorrect, check details or contact admin')
    return render(request, 'dashboard/staff.html')

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def dashboard(request):
    
    return render(request, 'dashboard/dashboard.html')

@login_required(login_url='/')
def post(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)

    if request.method == 'POST':
        postForm = BlogForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Images(blog=post_form, image=image)
                    photo.save()
            messages.success(request, "Posted Successfully")

            return redirect('/')
        else:
            print(postForm.errors, formset.errors)

    else:
        postForm = BlogForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    
    return render(request, 'dashboard/post-page.html', {'postForm' : postForm, 'formset' : formset})


@login_required(login_url='/')
def bolg_view(request):
    view_b = Blog.objects.all()
   

    return render(request, 'dashboard/quick-view.html', {'view': view_b})