# coaching/admin.py
from django.contrib import admin
from .models import CoachingStep1, CoachingStep2, CoachingStep3

@admin.register(CoachingStep1)
class CoachingStep1Admin(admin.ModelAdmin):
    list_display = ['id',
        'logo',
        'short_description',
        'detailed_description',
        'opens',
        'closes',
        'coaching_main_website',
        'contact_number',
        'email',
        'other_links',
        'facebook_page',
        'instagram_account',
        'linkedin_page',
        'youtube_channel',
        'pinterest_account',
        'twitter_handle',
        'name',
        'role',
        'email_mang',
        'contact_number_mang',
        'coaching_name',
        'coaching_gstin',
        'establishment_year',
        'pan_card_number',
        'pan_card_upload',
        'address_line_1',
        'address_line_2',
        'landmark',
        'pincode',
        'state',
        'city',
        'latitude',
        'longitude',
        'state',  # Location state
        'city',  # Location city
        'address_line_1_loc',
        'address_line_2_loc',
        'landmark_loc',
        'pincode_loc',
        'branch_name',
        'latitude_loc',
        'longitude_loc',]

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
    list_display = [

        'coaching_step2',
        'photo',
        'photo_description',
        'photo_keywords_meta_tags',
        'video_link',
        'video_file',
        'video_description',
        'video_keywords_meta_tags',
        'video_thumbnail',
        'review_name',
        'year_of_study',
        'course_taken',
        'overall_rating',
        'competitive_environment',
        'faculty_rating',
        'infrastructure_rating',
        'study_material_rating',
        'peer_learning_rating',
        'review_description',
        'review_links',
        'review_photo_or_video',
        'students_in_batch',
        'total_students',
        'number_of_faculty',
        'faq_question',
        'faq_answer',
        ]
