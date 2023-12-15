# coaching/admin.py
from django.contrib import admin
from .models import CoachingStep1, CoachingStep2, CoachingStep3

@admin.register(CoachingStep1)
class CoachingStep1Admin(admin.ModelAdmin):
    list_display = ['logo', 'short_description', 'detailed_description', 'coaching_main_website']

@admin.register(CoachingStep2)
class CoachingStep2Admin(admin.ModelAdmin):
    list_display = [
        'coaching_step1',
        'coaching_for_exams',
        'other_exams',
        'course_for_exam',
        'course_duration',
        'course_mode',
        'course_description',
        'total_fee',
        'discount',
        'study_material_included',
        'material_file',
        'material_description',
        'keywords_meta_tags',
        'links',
        'exams_who_can_refer',
        'excel_file',
        'result_photo',
        'result_name',
        'college_secured',
        'exam_cracked',
        'all_india_rank',
        'base_city_result',
        'testimonial',
        'faculty_photo',
        'faculty_name',
        'specialization',
        'background',
        'experience',
        'base_city_faculty',
        'faculty_links',
    ]

@admin.register(CoachingStep3)
class CoachingStep3Admin(admin.ModelAdmin):
    list_display = ['coaching_name', 'coaching_gstin', 'year_of_establishment', 'pan_card_no', 'address_line_1', 'address_line_2', 'pincode']
