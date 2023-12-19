# college/urls.py
from django.urls import path
from .views import CollegeCreateStep1View,CollegeCreateStep2View,CollegeCreateStep3View,CollegeCreateStep4View,CollegeCreateStep5View


urlpatterns = [
    path('step1/', CollegeCreateStep1View.as_view(), name='collegeCreate_step1'),
    path('step2/', CollegeCreateStep2View.as_view(), name='collegeCreate_step2'),
    path('step3/', CollegeCreateStep3View.as_view(), name='collegeCreate_step3'),
    path('step4/', CollegeCreateStep4View.as_view(), name='collegeCreate_step4'),
    path('step5/', CollegeCreateStep5View.as_view(), name='college_step5'),
]
