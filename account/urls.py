from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
 path('', views.user_login, name='login'),
 path('register/', views.register, name='register'),
#  path('', include('django.contrib.auth.urls')),
 path('edit/', views.edit, name="edit")
]