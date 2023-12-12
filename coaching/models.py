# coaching/models.py
from django.db import models

class Link(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=255)

class State(models.Model):
    name = models.CharField(max_length=255)

class StudyMaterial(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='study_materials/')
    description = models.TextField()

class College(models.Model):
    name = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)

class WeekDay(models.Model):
    name = models.CharField(max_length=15)

class Course(models.Model):
    name = models.CharField(max_length=15)

class Exam(models.Model):
    name = models.CharField(max_length=255)

class Facility(models.Model):
    name = models.CharField(max_length=255)

class Coaching(models.Model):
    # Step 1: Basic Details
    logo = models.ImageField(upload_to='coaching_logos/')
    short_description = models.TextField(max_length=250)
    detailed_description = models.TextField(max_length=500)
    days_of_operation = models.ManyToManyField(WeekDay)
    opens = models.TimeField()
    closes = models.TimeField()

    # Contact Details
    coaching_main_website = models.URLField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    other_links = models.ManyToManyField(Link, related_name='coaching_links')
    facebook_page = models.URLField()
    instagram_account = models.URLField()
    linkedin_page = models.URLField()
    youtube_channel = models.URLField()
    pinterest_account = models.URLField()
    twitter_handle = models.URLField()

    # Management Contact
    management_name = models.CharField(max_length=15)
    management_role = models.CharField(max_length=15)
    management_email = models.EmailField()
    management_contact = models.CharField(max_length=15)

    # Coaching Details
    coaching_name = models.CharField(max_length=15)
    coaching_gstin = models.CharField(max_length=10)
    year_of_establishment = models.PositiveIntegerField()
    pan_card_no = models.CharField(max_length=10)
    upload_pan_card = models.FileField(upload_to='coaching_pan_cards/')
    address_line_1 = models.TextField(max_length=50)
    address_line_2 = models.TextField(max_length=50)
    landmark_locality = models.CharField(max_length=10)
    pincode = models.PositiveIntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='coaching_state')
    city = models.CharField(max_length=50)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()

    # Locations
    locations_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='coaching_locations_state')
    locations_city = models.CharField(max_length=50)
    locations_address_line_1 = models.TextField(max_length=50)
    locations_address_line_2 = models.TextField(max_length=50)
    locations_landmark_locality = models.CharField(max_length=10)
    locations_pincode = models.PositiveIntegerField()
    locations_name_of_branch = models.CharField(max_length=10)
    locations_latitude = models.FloatField()
    locations_longitude = models.FloatField()

    # Step 2: Courses Offered and Its Details
    # Entrance Exams
    coaching_for_exams = models.ManyToManyField(Course, related_name='coaching_for_exams')
    other_exams = models.TextField()

    # Courses and Fees
    courses_for_exam = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coaching_courses_for_exam')
    course_duration = models.CharField(max_length=50)
    course_mode = models.CharField(max_length=50)
    course_description = models.TextField(max_length=500)
    total_fee = models.CharField(max_length=10)
    discount = models.CharField(max_length=10)
    study_material_included = models.BooleanField()

    # Study Material
    study_materials = models.ManyToManyField(StudyMaterial, related_name='coaching_study_materials')

    # Results
    results_excel_file = models.FileField(upload_to='coaching_results/')
    results_photo = models.ImageField(upload_to='coaching_results_photos/')
    results_name = models.CharField(max_length=10)
    results_college_secured = models.ForeignKey(College, on_delete=models.CASCADE, related_name='coaching_results_college_secured')
    results_exam_cracked = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='coaching_results_exam_cracked')
    results_all_india_rank = models.CharField(max_length=10)
    results_base_city = models.CharField(max_length=50)
    results_testimonial = models.TextField()

    # Faculties
    faculties_photo = models.ImageField(upload_to='coaching_faculties/')
    faculties_name = models.CharField(max_length=10)
    faculties_specialisation = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coaching_faculties_specialisation')
    faculties_background = models.CharField(max_length=50)
    faculties_experience = models.CharField(max_length=50)
    faculties_base_city = models.CharField(max_length=50)
    faculties_links = models.TextField()

    # Step 3: Additional Details
    # Photos
    photos_photo = models.ImageField(upload_to='coaching_photos/')
    photos_description = models.TextField(max_length=250)
    photos_category = models.ManyToManyField(Category, related_name='coaching_photos_categories')
    photos_keywords_meta_tags = models.TextField()

    # Videos
    videos_link = models.URLField()
    videos_file = models.FileField(upload_to='coaching_videos/')
    videos_description = models.TextField(max_length=250)
    videos_keywords_meta_tags = models.TextField()
    videos_thumbnail = models.ImageField(upload_to='coaching_videos_thumbnails/')

    # Reviews
    reviews_name = models.CharField(max_length=10)
    reviews_year_of_study = models.CharField(max_length=50)
    reviews_course_taken = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='coaching_reviews_course_taken')
    reviews_overall_rating = models.PositiveIntegerField()
    reviews_competitive_environment = models.PositiveIntegerField()
    reviews_faculty = models.PositiveIntegerField()
    reviews_infrastructure = models.PositiveIntegerField()
    reviews_study_material = models.PositiveIntegerField()
    reviews_peer_learning = models.PositiveIntegerField()
    reviews_detailed_description = models.TextField()
    reviews_links = models.URLField()
    reviews_photo_video = models.ImageField(upload_to='coaching_reviews_photo_video/')

    # Checklist
    checklist_available_facilities = models.ManyToManyField(Facility, related_name='coaching_checklist_facilities')
    checklist_students_in_batch = models.CharField(max_length=5)
    checklist_total_students_in_coaching = models.CharField(max_length=5)
    checklist_number_of_faculty = models.CharField(max_length=5)

    # Frequently Asked Questions
    faqs_question = models.TextField()
    faqs_answer = models.TextField()
