# coaching/models.py
from django.db import models

class Link(models.Model):
    url = models.TextField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)

class State(models.Model):
    name = models.CharField(blank=True, null=True)

class StudyMaterial(models.Model):
    name = models.CharField(blank=True, null=True)
    file = models.FileField(upload_to='study_materials/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class College(models.Model):
    name = models.CharField(blank=True, null=True)

class Category(models.Model):
    name = models.CharField(blank=True, null=True)



class Course(models.Model):
    name = models.CharField(blank=True, null=True)

class Exam(models.Model):
    name = models.CharField(blank=True, null=True)

class PhotoCategory(models.Model):
    name = models.CharField(blank=True, null=True)

class Facility(models.Model):
    name = models.CharField(blank=True, null=True)

class CoachingSteps1(models.Model):
    # Step 1: Basic Details

    #1. About
    logo = models.ImageField(upload_to='coaching_logos/', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)
    days_of_operation = models.TextField(blank=True, null=True)
    opens = models.TimeField(blank=True, null=True)
    closes = models.TimeField(blank=True, null=True)

    #2. Contact Details
    coaching_main_website = models.TextField(blank=True, null=True)
    contact_number = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # Other websites/important links
    other_links = models.TextField(blank=True, null=True)
    # Facebook page
    facebook_page = models.TextField(blank=True, null=True)
    # Instagram account
    instagram_account = models.TextField(blank=True, null=True)
    # LinkedIn page
    linkedin_page = models.TextField(blank=True, null=True)
    # Youtube Channel
    youtube_channel = models.TextField(blank=True, null=True)
    # Pinterest Account
    pinterest_account = models.TextField(blank=True, null=True)
    # Twitter handle
    twitter_handle = models.TextField(blank=True, null=True)

    #3. Management Contact
    # Name
    name = models.CharField(blank=True, null=True)
    # Role in Institute
    role = models.CharField(blank=True, null=True)
    # Email ID
    email_mang = models.EmailField(blank=True, null=True)
    # Contact Number
    contact_number_mang = models.CharField(blank=True, null=True)

    #4. Coaching Details
    # Coaching name
    coaching_name = models.CharField(blank=True, null=True)
    # Coaching GSTIN
    coaching_gstin = models.CharField(blank=True, null=True)
    # Year of Establishment
    establishment_year = models.PositiveIntegerField(blank=True, null=True)
    # PAN card No.
    pan_card_number = models.CharField(blank=True, null=True)
    # Upload PAN card
    pan_card_upload = models.FileField(upload_to='pan_cards/',blank=True, null=True)
    # Address line 1
    address_line_1 = models.CharField(blank=True, null=True)
    # Address line 2
    address_line_2 = models.CharField(blank=True, null=True)
    # Landmark/Locality
    landmark = models.CharField(blank=True, null=True)
    # Pincode
    pincode = models.PositiveIntegerField(blank=True, null=True)
    # State
    STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
    ]
    state = models.CharField( choices=STATE_CHOICES, blank=True, null=True)
    # City
    city = models.CharField(blank=True, null=True)
    # Location - Latitude and Longitude
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

 # Location
    # State
    STATE_CHOICES = [
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry'),
    ]
    state_loc = models.CharField( choices=STATE_CHOICES,blank=True, null=True)
    # City
    city_loc = models.CharField(blank=True, null=True)
    # Address Line 1
    address_line_1_loc = models.CharField(blank=True, null=True)
    # Address Line 2
    address_line_2_loc = models.CharField(blank=True, null=True)
    # Landmark/Locality
    landmark_loc = models.CharField(blank=True, null=True)
    # Pincode
    pincode_loc = models.PositiveIntegerField(blank=True, null=True)
    # Name of Branch
    branch_name = models.CharField(blank=True, null=True)
    # Location - Latitude and Longitude
    latitude_loc = models.FloatField(blank=True, null=True)
    longitude_loc = models.FloatField(blank=True, null=True)

    # ... add other fields for step 1

class CoachingSteps2(models.Model):

    # Entrance Exams
    coaching_for_exams = models.TextField(blank=True, null=True)
    other_exams = models.TextField(blank=True, null=True)

    # Courses and Fees
    course_for_exam = models.TextField(blank=True, null=True)
    course_duration = models.TextField(blank=True, null=True)
    course_mode = models.CharField( choices=[('online', 'Online'), ('offline', 'Offline')],blank=True, null=True)
    course_description = models.TextField( blank=True, null=True)
    total_fee = models.CharField( blank=True, null=True)
    discount = models.CharField( blank=True, null=True)
    study_material_included = models.CharField( choices=[('yes', 'Yes'), ('no', 'No')],blank=True, null=True)

    # Study Material
    material_file = models.FileField(upload_to='material_files/',blank=True, null=True)
    material_description = models.TextField( blank=True, null=True)
    keywords_meta_tags = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    exams_who_can_refer = models.CharField( choices=[('exam1', 'Exam 1'), ('exam2', 'Exam 2')],blank=True, null=True)

    # Results
    excel_file = models.FileField(upload_to='result_files/',blank=True, null=True)
    result_photo = models.ImageField(upload_to='result_photos/',blank=True, null=True)
    result_name = models.CharField( blank=True, null=True)
    college_secured = models.TextField(blank=True, null=True)
    exam_cracked = models.CharField( choices=[('exam1', 'Exam 1'), ('exam2', 'Exam 2')],blank=True, null=True)
    all_india_rank = models.TextField( blank=True, null=True)
    base_city_result = models.TextField( blank=True, null=True)
    testimonial = models.TextField( blank=True, null=True)

    # Faculties
    faculty_photo = models.ImageField(upload_to='faculty_photos/',blank=True, null=True)
    faculty_name = models.CharField( blank=True, null=True)
    specialization = models.TextField(blank=True, null=True)
    background = models.TextField( blank=True, null=True)
    experience = models.TextField( blank=True, null=True)
    base_city_faculty = models.TextField( blank=True, null=True)
    faculty_links = models.TextField(blank=True, null=True)




class CoachingSteps3(models.Model):

    # Photos
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    photo_description = models.TextField( blank=True, null=True)
    photo_category = models.TextField(blank=True, null=True)
    photo_keywords_meta_tags = models.TextField( blank=True, null=True)

    # Videos
    video_link = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_description = models.TextField( blank=True, null=True)
    video_keywords_meta_tags = models.TextField( blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)

    # Reviews
    review_name = models.CharField( blank=True, null=True)
    year_of_study = models.TextField(blank=True, null=True)
    course_taken = models.TextField(blank=True, null=True)
    overall_rating = models.IntegerField(choices=range(1, 6), blank=True, null=True)
    competitive_environment = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    faculty_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    infrastructure_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    overall_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    peer_learning_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    study_material_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    review_description = models.TextField( blank=True, null=True)
    review_links = models.TextField(blank=True, null=True)
    review_photo_or_video = models.FileField(upload_to='review_files/', blank=True, null=True)

    # Checklist
    available_facilities = models.CharField(blank=True, null=True)
    students_in_batch = models.CharField( blank=True, null=True)
    total_students = models.CharField( blank=True, null=True)
    number_of_faculty = models.CharField( blank=True, null=True)

    # Frequently Asked Questions
    faq_question = models.TextField(blank=True, null=True)
    faq_answer = models.TextField(blank=True, null=True)



