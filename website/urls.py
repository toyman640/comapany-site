from django.urls import path
from website import views


app_name = 'website'

urlpatterns = [
   path('about-us/', views.about, name='about'),
   path('our-services/', views.service, name='service'),
   path('contact-us/', views.contact, name='contact')

]