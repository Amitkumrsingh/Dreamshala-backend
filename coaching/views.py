from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CoachingSteps1, CoachingSteps2, CoachingSteps3
from .serializers import CoachingStep1Serializer, CoachingStep2Serializer, CoachingStep3Serializer

class CoachingCreateStep1View(generics.CreateAPIView):
    serializer_class = CoachingStep1Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class CoachingCreateStep2View(generics.CreateAPIView):
    serializer_class = CoachingStep2Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class CoachingCreateStep3View(generics.CreateAPIView):
    serializer_class = CoachingStep3Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
