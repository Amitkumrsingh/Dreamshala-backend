
# serializers.py in college app
from rest_framework import serializers
from .models import CollegeStep1, CollegeStep2, CollegeStep3, CollegeStep4, CollegeStep5

class CollegeStep1Serializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeStep1
        fields = '__all__'

class CollegeStep2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeStep2
        fields = '__all__'

class CollegeStep3Serializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeStep3
        fields = '__all__'

class CollegeStep4Serializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeStep4
        fields = '__all__'

class CollegeStep5Serializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeStep5
        fields = '__all__'
