# exam/urls.py
from django.urls import path
from .views import ExamListCreateView


urlpatterns = [
    path('exams/', ExamListCreateView.as_view(), name='exam-list-create'),

]
