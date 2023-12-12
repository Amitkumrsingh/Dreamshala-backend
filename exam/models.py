# exam/models.py
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=255)

class Link(models.Model):
    url = models.URLField()

class PaymentMode(models.Model):
    name = models.CharField(max_length=255)

class RegistrationCategory(models.Model):
    name = models.CharField(max_length=255)

class ExamDate(models.Model):
    date = models.DateField()

class ExamPattern(models.Model):
    excel_file = models.FileField(upload_to='exam_patterns/')
    degree_branch = models.CharField(max_length=255)
    mode_of_examination = models.CharField(max_length=100, choices=[('online', 'Online'), ('offline', 'Offline')])
    duration_of_examination = models.CharField(max_length=100, choices=[('1_hour', '1 Hour'), ('2_hours', '2 Hours'), ('3_hours', '3 Hours')])
    number_of_questions = models.IntegerField()
    total_marks = models.IntegerField()
    subjects_sections = models.TextField()
    medium_of_paper = models.TextField()
    describe_type_of_questions = models.TextField()
    describe_marking_scheme = models.TextField()

class StudyMaterial(models.Model):
    media_file = models.FileField(upload_to='study_materials/')
    description = models.TextField(max_length=500)
    keywords_meta_tags = models.TextField()
    material_category = models.CharField(max_length=255, choices=[('books', 'Books'), ('videos', 'Videos'), ('pdf', 'PDF')])

class PreviousYearPaper(models.Model):
    pdf_files = models.FileField(upload_to='previous_year_papers/')
    year_of_paper = models.IntegerField()
    date_of_paper = models.DateField()
    mode_of_paper = models.CharField(max_length=100, choices=[('online', 'Online'), ('offline', 'Offline')])
    description_to_paper = models.TextField(max_length=500)

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Exam(models.Model):
    # Step 1: Basic Details
    logo = models.ImageField(upload_to='exam_logos/')
    short_description = models.TextField(max_length=200)
    detailed_description = models.TextField(max_length=500)
    exam_frequency = models.CharField(max_length=100, choices=[('daily', 'Daily'), ('weekly', 'Weekly')])
    exam_mode = models.CharField(max_length=100, choices=[('online', 'Online'), ('offline', 'Offline')])
    states_applicable = models.ManyToManyField(State, related_name='exams')

    # Contact Details
    exam_official_website = models.URLField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    other_links = models.ManyToManyField(Link, related_name='exams')

    # Brochure
    brochure = models.FileField(upload_to='exam_brochures/')
    brochure_description = models.TextField(max_length=500)
    keywords = models.TextField(max_length=200)
    brochure_links = models.ManyToManyField(Link, related_name='brochures')
    exams_who_can_refer = models.ManyToManyField('self', related_name='referring_exams')

    # Registration Details
    registration_website = models.URLField()
    registration_mode = models.CharField(max_length=100, choices=[('online', 'Online'), ('offline', 'Offline')])
    payment_modes = models.ManyToManyField(PaymentMode, related_name='exams')
    registration_categories = models.ManyToManyField(RegistrationCategory, related_name='exams')

    # Step 2: Important Updates
    important_news = models.TextField()
    news_category = models.CharField(max_length=50, choices=[('very_imp', 'Very Important'), ('imp', 'Important'), ('medium_imp', 'Medium Important'), ('less_imp', 'Less Important')])
    important_dates_start = models.DateField()
    important_dates_end = models.DateField()
    admit_card_release_date = models.DateField()
    result_date = models.DateField()

    # Exam Dates
    exam_dates = models.ManyToManyField(ExamDate, related_name='exams')

    # Exam Patterns
    exam_patterns = models.ManyToManyField(ExamPattern, related_name='exams')

    # Study Materials
    study_materials = models.ManyToManyField(StudyMaterial, related_name='exams')

    # Previous Year Question Papers
    previous_year_papers = models.ManyToManyField(PreviousYearPaper, related_name='exams')

    # Frequently Asked Questions
    faqs = models.ManyToManyField(FAQ, related_name='exams')
