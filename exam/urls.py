# exam/urls.py

from django.urls import path
from .views import ExamCreateStep1View, ExamCreateStep2View, ExamCreateStep3View

urlpatterns = [
    path('step1/', ExamCreateStep1View.as_view(), name='exam-create-step1'),
    path('step2/', ExamCreateStep2View.as_view(), name='exam-create-step2'),
    path('step3/', ExamCreateStep3View.as_view(), name='exam-create-step3'),
]
