# coaching/views.py
from rest_framework import generics
from .models import Coaching
from .serializers import CoachingSerializer

class CoachingListCreateView(generics.ListCreateAPIView):
    queryset = Coaching.objects.all()
    serializer_class = CoachingSerializer