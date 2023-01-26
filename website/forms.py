from django import forms
from .models import *



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'authur', 'write_up')



class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image',)