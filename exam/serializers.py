# exam/serializers.py
from rest_framework import serializers
from .models import Exam, State, Link, PaymentMode, RegistrationCategory, ExamDate, ExamPattern, StudyMaterial, PreviousYearPaper, FAQ

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

class PaymentModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = '__all__'

class RegistrationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationCategory
        fields = '__all__'

class ExamDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamDate
        fields = '__all__'

class ExamPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamPattern
        fields = '__all__'

class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = '__all__'

class PreviousYearPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearPaper
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    states_applicable = StateSerializer(many=True)
    other_links = LinkSerializer(many=True)
    brochure_links = LinkSerializer(many=True)
    exams_who_can_refer = serializers.PrimaryKeyRelatedField(many=True, queryset=Exam.objects.all())
    payment_modes = PaymentModeSerializer(many=True)
    registration_categories = RegistrationCategorySerializer(many=True)
    exam_dates = ExamDateSerializer(many=True)
    exam_patterns = ExamPatternSerializer(many=True)
    study_materials = StudyMaterialSerializer(many=True)
    previous_year_papers = PreviousYearPaperSerializer(many=True)
    faqs = FAQSerializer(many=True)

    class Meta:
        model = Exam
        fields = '__all__'
