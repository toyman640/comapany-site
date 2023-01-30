from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('post/', views.post, name='post'),
    path('post-view/', views.bolg_view, name='blog_view')
]