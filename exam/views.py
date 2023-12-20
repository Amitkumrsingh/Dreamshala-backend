from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ExamStep1, ExamStep2, ExamStep3
from .serializers import ExamStep1Serializer, ExamStep2Serializer, ExamStep3Serializer

class ExamCreateStep1View(generics.CreateAPIView):
    serializer_class = ExamStep1Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class ExamCreateStep2View(generics.CreateAPIView):
    serializer_class = ExamStep2Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

class ExamCreateStep3View(generics.CreateAPIView):
    serializer_class = ExamStep3Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
