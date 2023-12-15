# coaching/urls.py
from django.urls import path
from .views import CoachingCreateStep1View, CoachingCreateStep2View, CoachingCreateStep3View

urlpatterns = [
    path('Step1/', CoachingCreateStep1View.as_view(), name='Basic Details'),
    path('Step2/', CoachingCreateStep2View.as_view(), name='Courses Offered and Its Details'),
    path('Step3/', CoachingCreateStep3View.as_view(), name='Additional Details'),
]
