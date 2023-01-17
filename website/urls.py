from django.urls import path
from website import views


app_name = 'website'

urlpatterns = [
   path('about-us/', views.about, name='about'),
   path('our-services/', views.service, name='service'),
   path('contact-us/', views.contact, name='contact'),
   path('blog-post/', views.blog, name='blog'),
   path('post-detail/', views.blog_detail, name='blog_detail')
]