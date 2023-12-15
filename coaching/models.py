# coaching/models.py
from django.db import models

class Link(models.Model):
    url = models.URLField(blank=True, null=True)
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

class WeekDay(models.Model):
    day_name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.day_name

class Course(models.Model):
    name = models.CharField(blank=True, null=True)

class Exam(models.Model):
    name = models.CharField(blank=True, null=True)

class PhotoCategory(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)

class Facility(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)

class CoachingStep1(models.Model):
    # Step 1: Basic Details

    #1. About
    logo = models.ImageField(upload_to='coaching_logos/', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)
    days_of_operation = models.ManyToManyField(WeekDay)
    opens = models.TimeField(blank=True, null=True)
    closes = models.TimeField(blank=True, null=True)

    #2. Contact Details
    coaching_main_website = models.URLField(blank=True, null=True)
    contact_number = models.CharField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # Other websites/important links
    other_links = models.URLField(blank=True, null=True)
    # Facebook page
    facebook_page = models.URLField(blank=True, null=True)
    # Instagram account
    instagram_account = models.URLField(blank=True, null=True)
    # LinkedIn page
    linkedin_page = models.URLField(blank=True, null=True)
    # Youtube Channel
    youtube_channel = models.URLField(blank=True, null=True)
    # Pinterest Account
    pinterest_account = models.URLField(blank=True, null=True)
    # Twitter handle
    twitter_handle = models.URLField(blank=True, null=True)

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
    address_line_1 = models.CharField(blank=True, null=True, default='Hydrabad')
    # Address line 2
    address_line_2 = models.CharField(blank=True, null=True, default='Hydrabad')
    # Landmark/Locality
    landmark = models.CharField(blank=True, null=True)
    # Pincode
    pincode = models.PositiveIntegerField(blank=True, null=True)
    # State
    STATE_CHOICES = [
        ('State1', 'State 1'),
        ('State2', 'State 2'),
        # Add more states as needed
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES, blank=True, null=True)
    # City
    city = models.CharField(blank=True, null=True)
    # Location - Latitude and Longitude
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

 # Location
    # State
    STATE_CHOICES = [
        ('State1', 'State 1'),
        ('State2', 'State 2'),
        # Add more states as needed
    ]
    state = models.CharField(max_length=20, choices=STATE_CHOICES,blank=True, null=True)
    # City
    city = models.CharField(blank=True, null=True)
    # Address Line 1
    address_line_1_loc = models.CharField(blank=True, null=True , default='Hyderabad')
    # Address Line 2
    address_line_2_loc = models.CharField(blank=True, null=True , default='Hyderabad')
    # Landmark/Locality
    landmark = models.CharField(blank=True, null=True)
    # Pincode
    pincode = models.PositiveIntegerField(blank=True, null=True)
    # Name of Branch
    branch_name = models.CharField(blank=True, null=True, default='Hyderabad')
    # Location - Latitude and Longitude
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    # ... add other fields for step 1

class CoachingStep2(models.Model):
    coaching_step1 = models.OneToOneField(CoachingStep1, on_delete=models.CASCADE, primary_key=True)

    # Entrance Exams
    coaching_for_exams = models.CharField(max_length=50, choices=[('design', 'Design'), ('engineering', 'Engineering'), ('etc', 'Etc.')],blank=True, null=True)
    other_exams = models.TextField(blank=True, null=True)

    # Courses and Fees
    course_for_exam = models.CharField(max_length=50, choices=[('course1', 'Course 1'), ('course2', 'Course 2'), ('course3', 'Course 3')],blank=True, null=True)
    course_duration = models.CharField(max_length=50, choices=[('duration1', 'Duration 1'), ('duration2', 'Duration 2')],blank=True, null=True)
    course_mode = models.CharField(max_length=50, choices=[('mode1', 'Mode 1'), ('mode2', 'Mode 2')],blank=True, null=True)
    course_description = models.TextField(max_length=500 , blank=True, null=True)
    total_fee = models.CharField(max_length=10, blank=True, null=True)
    discount = models.CharField(max_length=10, blank=True, null=True)
    study_material_included = models.CharField(max_length=50, choices=[('yes', 'Yes'), ('no', 'No')],blank=True, null=True)

    # Study Material
    material_file = models.FileField(upload_to='material_files/',blank=True, null=True)
    material_description = models.TextField(max_length=500, blank=True, null=True)
    keywords_meta_tags = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    exams_who_can_refer = models.CharField(max_length=50, choices=[('exam1', 'Exam 1'), ('exam2', 'Exam 2')],blank=True, null=True)

    # Results
    excel_file = models.FileField(upload_to='result_files/',blank=True, null=True)
    result_photo = models.ImageField(upload_to='result_photos/',blank=True, null=True)
    result_name = models.CharField(max_length=10, blank=True, null=True)
    college_secured = models.CharField(max_length=50, choices=[('college1', 'College 1'), ('college2', 'College 2')],blank=True, null=True)
    exam_cracked = models.CharField(max_length=50, choices=[('exam1', 'Exam 1'), ('exam2', 'Exam 2')],blank=True, null=True)
    all_india_rank = models.CharField(max_length=50, choices=[('rank1', 'Rank 1'), ('rank2', 'Rank 2')],blank=True, null=True)
    base_city_result = models.CharField(max_length=50, choices=[('city1', 'City 1'), ('city2', 'City 2')],blank=True, null=True)
    testimonial = models.TextField(max_length=500, blank=True, null=True)

    # Faculties
    faculty_photo = models.ImageField(upload_to='faculty_photos/',blank=True, null=True)
    faculty_name = models.CharField(max_length=10, blank=True, null=True)
    specialization = models.CharField(max_length=50, choices=[('spec1', 'Specialization 1'), ('spec2', 'Specialization 2')],blank=True, null=True)
    background = models.CharField(max_length=50, choices=[('bg1', 'Background 1'), ('bg2', 'Background 2')],blank=True, null=True)
    experience = models.CharField(max_length=50, choices=[('exp1', 'Experience 1'), ('exp2', 'Experience 2')],blank=True, null=True)
    base_city_faculty = models.CharField(max_length=50, choices=[('city1', 'City 1'), ('city2', 'City 2')],blank=True, null=True)
    faculty_links = models.TextField(blank=True, null=True)




class CoachingStep3(models.Model):
    coaching_step2 = models.OneToOneField(CoachingStep2, on_delete=models.CASCADE, primary_key=True)


    # Photos
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    photo_description = models.TextField(max_length=250, blank=True, null=True)
    photo_category = models.ManyToManyField('PhotoCategory', blank=True)
    photo_keywords_meta_tags = models.TextField(max_length=200, blank=True, null=True)

    # Videos
    video_link = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    video_description = models.TextField(max_length=250, blank=True, null=True)
    video_keywords_meta_tags = models.TextField(max_length=200, blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)

    # Reviews
    review_name = models.CharField(max_length=10, blank=True, null=True)
    year_of_study = models.CharField(max_length=10, choices=[('year1', 'Year 1'), ('year2', 'Year 2')], blank=True, null=True)
    course_taken = models.CharField(max_length=50, choices=[('course1', 'Course 1'), ('course2', 'Course 2')], blank=True, null=True)
    overall_rating = models.IntegerField(choices=range(1, 6), blank=True, null=True)
    competitive_environment = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    faculty_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    infrastructure_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    overall_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    peer_learning_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    study_material_rating = models.IntegerField(choices=enumerate(range(1, 6)), blank=True, null=True)
    review_description = models.TextField(max_length=500, blank=True, null=True)
    review_links = models.URLField(blank=True, null=True)
    review_photo_or_video = models.FileField(upload_to='review_files/', blank=True, null=True)

    # Checklist
    available_facilities = models.ManyToManyField('Facility', blank=True)
    students_in_batch = models.CharField(max_length=5, blank=True, null=True)
    total_students_in_coaching = models.CharField(max_length=5, blank=True, null=True)
    number_of_faculty = models.CharField(max_length=5, blank=True, null=True)

    # Frequently Asked Questions
    faq_question = models.TextField(blank=True, null=True)
    faq_answer = models.TextField(blank=True, null=True)



