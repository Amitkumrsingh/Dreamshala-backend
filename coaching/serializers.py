# coaching/serializers.py
from rest_framework import serializers
from .models import CoachingSteps1, CoachingSteps2, CoachingSteps3

class CoachingStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingSteps1
        fields = '__all__'

class CoachingStep2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingSteps2
        fields = '__all__'

class CoachingStep3Serializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingSteps3
        fields = '__all__'
