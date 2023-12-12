# coaching/serializers.py
from rest_framework import serializers
from .models import Coaching

class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaching
        fields = '__all__'