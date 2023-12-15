# coaching/serializers.py
from rest_framework import serializers
from .models import CoachingStep1, CoachingStep2, CoachingStep3

class CoachingStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingStep1
        fields = '__all__'

class CoachingStep2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingStep2
        fields = '__all__'

class CoachingStep3Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingStep3
        fields = '__all__'
