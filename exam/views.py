# exam/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ExamStep1, ExamStep2, ExamStep3
from .serializers import ExamStep1Serializer, ExamStep2Serializer, ExamStep3Serializer

class ExamCreateStep1View(generics.CreateAPIView):
    serializer_class = ExamStep1Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 1 data
        # Save or process step 1 data as needed
        return Response({'message': 'Step 1 data received'}, status=status.HTTP_201_CREATED)

class ExamCreateStep2View(generics.CreateAPIView):
    serializer_class = ExamStep2Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 2 data
        # Save or process step 2 data as needed
        return Response({'message': 'Step 2 data received'}, status=status.HTTP_201_CREATED)

class ExamCreateStep3View(generics.CreateAPIView):
    serializer_class = ExamStep3Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 3 data
        # Save or process step 3 data as needed
        return Response({'message': 'Step 3 data received'}, status=status.HTTP_201_CREATED)
