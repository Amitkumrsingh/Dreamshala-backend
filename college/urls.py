# college/urls.py
from django.urls import path
from .views import CollegeListCreateView

urlpatterns = [
    path('colleges/', CollegeListCreateView.as_view(), name='college-list-create'),
]