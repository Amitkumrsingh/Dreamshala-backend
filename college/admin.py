# coaching/admin.py
# college/admin.py
from django.contrib import admin
from .models import CollegeStep1, CollegeStep2, CollegeStep3, CollegeStep4, CollegeStep5

@admin.register(CollegeStep1)
class CollegeStep1Admin(admin.ModelAdmin):
    list_display = ('id',
        'logo',
        'short_description',
        'detailed_description',
        'days_of_operation',
        'opens',
        'closes',
        'main_website',
        'contact_number',
        'email',
        'other_links',
        'facebook_page',
        'instagram_account',
        'linkedin_page',
        'youtube_channel',
        'pinterest_account',
        'twitter_handle',
        'college_name',
        'GSTIN',
        'establishment_year',
        'college_address_line_1',
        'college_address_line_2',
        'college_landmark_locality',
        'college_pincode',
        'college_state',
        'college_city',
        'college_pan_card_number',
        'college_pan_card_upload',
        'state',  # Location state
        'city',  # Location city
        'address_line_1',
        'address_line_2',
        'landmark_locality',
        'pincode',
        'state',  # Location state
        'city',  # Location city
        'latitude',
        'longitude',
        'management_name',
        'management_role',
        'management_email',
        'management_contact',
        )


@admin.register(CollegeStep2)
class CollegeStep2Admin(admin.ModelAdmin):
    list_display = ('id',
        'important_news',
        'news_category',
        'date_description',
        'starts_from',
        'ends_at',
        'event_description',)

@admin.register(CollegeStep3)
class CollegeStep3Admin(admin.ModelAdmin):
    list_display = ('id',
    'course',
    'course_duration',
    'degree_offered',
    'course_description',
    'total_fees',
    'course_mode',
    'eligibility_criteria',
    'batch_strength',
    'degree_branch_application_process',
    'application_process_description',
    'eligibility_criteria_description',
    'degree_branch',
    'parameter_of_cutoffs',
    'category',
    'percentile',
    'subject',
    'subject_category',
    'cutoff_percentile',)  # Add other fields as needed

@admin.register(CollegeStep4)
class CollegeStep4Admin(admin.ModelAdmin):
    list_display = ('id',
    'photo',
    'degree',
    'year_of_graduation',
    'experience',
    'latest_position_achievement',
    'links',
    'name',
    'specialisation',
    'background',
    'experience',  # Note: This field is repeated; you might want to change one of them
    'base_city',
    'faculty_links',)  # Add other fields as needed

@admin.register(CollegeStep5)
class CollegeStep5Admin(admin.ModelAdmin):
    list_display = ('id',
    'degree_branch',
    'overall_placement_description',
    'number_of_recruiters',
    'number_of_offers',
    'number_of_international_offers',
    'to_recruiters',
    'highest_package',
    'average_package',
    'photo',
    'photo_description',
    'photo_category',
    'photo_keywords_meta_tags',
    'video_link',
    'video_file',
    'video_description',
    'video_keywords_meta_tags',
    'video_thumbnail',
    'name',
    'year_of_study',
    'course_taken',
    'overall_rating',
    'academics_rating',
    'faculty_rating',
    'infrastructure_rating',
    'accommodation_rating',
    'placement_rating',
    'social_life_rating',
    'detailed_description',
    'links',
    'photo_video',
    'available_facilities',
    'students_in_batch',
    'total_students',
    'number_of_faculty',
    'faq_question',
    'faq_answer',
    )  # Add other fields as needed
