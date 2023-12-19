# college/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CollegeStep1, CollegeStep2, CollegeStep3, CollegeStep4, CollegeStep5
from .serializers import CollegeStep1Serializer,CollegeStep2Serializer,CollegeStep3Serializer,CollegeStep4Serializer,CollegeStep5Serializer


class CollegeCreateStep1View(generics.CreateAPIView):
    serializer_class = CollegeStep1Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 1 data
        # Save or process step 1 data as needed
        return Response({'message': 'Step 1 data received'}, status=status.HTTP_201_CREATED)

class CollegeCreateStep2View(generics.CreateAPIView):
    serializer_class = CollegeStep2Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 2 data
        # Save or process step 2 data as needed
        return Response({'message': 'Step 2 data received'}, status=status.HTTP_201_CREATED)

class CollegeCreateStep3View(generics.CreateAPIView):
    serializer_class = CollegeStep3Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 3 data
        # Save or process step 3 data as needed
        return Response({'message': 'Step 3 data received'}, status=status.HTTP_201_CREATED)

class CollegeCreateStep4View(generics.CreateAPIView):
    serializer_class = CollegeStep4Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 4 data
        # Save or process step 4 data as needed
        return Response({'message': 'Step 4 data received'}, status=status.HTTP_201_CREATED)

class CollegeCreateStep5View(generics.CreateAPIView):
    serializer_class = CollegeStep5Serializer

    def create(self, request, *args, **kwargs):
        # Handle step 5 data
        # Save or process step 5 data as needed
        return Response({'message': 'Step 5 data received'}, status=status.HTTP_201_CREATED)

