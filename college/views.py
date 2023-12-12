# college/views.py
from rest_framework import generics
from .models import College
from .serializers import CollegeSerializer

class CollegeListCreateView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer