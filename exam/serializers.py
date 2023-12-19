# exam/serializers.py

from rest_framework import serializers
from .models import ExamStep1, ExamStep2, ExamStep3

class ExamStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStep1
        fields = '__all__'

class ExamStep2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStep2
        fields = '__all__'

class ExamStep3Serializer(serializers.ModelSerializer):
    class Meta:
        model = ExamStep3
        fields = '__all__'
