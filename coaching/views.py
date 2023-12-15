# coaching/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CoachingStep1, CoachingStep2, CoachingStep3
from .serializers import CoachingStep1Serializer, CoachingStep2Serializer, CoachingStep3Serializer

class CoachingCreateStep1View(generics.CreateAPIView):
    serializer_class = CoachingStep1Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 1 data
        # Save or process step 1 data as needed
        return Response({'message': 'Step 1 data received'}, status=status.HTTP_201_CREATED)

class CoachingCreateStep2View(generics.CreateAPIView):
    serializer_class = CoachingStep2Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 2 data
        # Save or process step 2 data as needed
        return Response({'message': 'Step 2 data received'}, status=status.HTTP_201_CREATED)

class CoachingCreateStep3View(generics.CreateAPIView):
    serializer_class = CoachingStep3Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 3 data
        # Save or process step 3 data as needed
        return Response({'message': 'Step 3 data received'}, status=status.HTTP_201_CREATED)
