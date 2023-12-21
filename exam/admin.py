# exam/admin.py

from django.contrib import admin
from .models import ExamStep1, ExamStep2, ExamStep3

@admin.register(ExamStep1)
class ExamStep1Admin(admin.ModelAdmin):
    list_display = ('id',
    'logo',
    'short_description',
    'detailed_description',
    'exam_frequency',
    'exam_mode',
    'states_applicable',
    'exam_official_website',
    'contact_number',
    'email',
    'other_links',
    'upload_brochure',
    'brochure_description',
    'keywords_meta_tags',
    'brochure_links',
    'exams_who_can_refer',
    'registration_website',
    'registration_mode',
    'payment_modes',
    'category',
    'fee',
    'registration_fees',)  # Add other fields as needed

@admin.register(ExamStep2)
class ExamStep2Admin(admin.ModelAdmin):
    list_display = ('id',
    'news_post',
    'news_category',
    'registration_start_date',
    'registration_end_date',
    'admit_card_release_date',
    'result_date',
    'exam_dates',)  # Add other fields as needed

@admin.register(ExamStep3)
class ExamStep3Admin(admin.ModelAdmin):
    list_display = ('id',
    'excel_file',
        'pattern_degree_branch',
        'pattern_mode',
        'pattern_duration',
        'pattern_questions',
        'pattern_total_marks',
        'pattern_subjects_sections',
        'pattern_medium',
        'pattern_type_of_questions',
        'pattern_marking_scheme',
        'material_file',
        'material_description',
        'material_keywords',
        'material_category',
        'material_exam_ref',
        'material_links',
        'question_paper_files',
        'question_paper_exam',
        'question_paper_year',
        'question_paper_date',
        'question_paper_mode',
        'question_paper_description',
        'question_paper_links',
        'question',
        'answer',)  # Add other fields as needed
