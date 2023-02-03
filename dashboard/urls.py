from django.urls import path
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login-page/', views.login_page, name='login_page'),
    path('post/', views.post, name='post'),
    path('post-view/', views.bolg_view, name='blog_view'),
    path('logout/', views.logout_view, name='logout_view')
]