# college/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CollegeStep1, CollegeStep2, CollegeStep3, CollegeStep4, CollegeStep5
from .serializers import CollegeStep1Serializer, CollegeStep2Serializer, CollegeStep3Serializer, CollegeStep4Serializer, CollegeStep5Serializer

class CollegeCreateStep1View(generics.CreateAPIView):
    serializer_class = CollegeStep1Serializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class CollegeCreateStep2View(generics.CreateAPIView):
    serializer_class = CollegeStep2Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class CollegeCreateStep3View(generics.CreateAPIView):
    serializer_class = CollegeStep3Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class CollegeCreateStep4View(generics.CreateAPIView):
    serializer_class = CollegeStep4Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class CollegeCreateStep5View(generics.CreateAPIView):
    serializer_class = CollegeStep5Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
