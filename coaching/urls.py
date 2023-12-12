# coaching/urls.py
from django.urls import path
from .views import CoachingListCreateView

urlpatterns = [
    path('coaching/', CoachingListCreateView.as_view(), name='coaching-list-create'),
]