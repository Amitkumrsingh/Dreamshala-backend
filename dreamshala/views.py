# Dreamshala/views.py

from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Dshala!")

# You can add more views as needed

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

