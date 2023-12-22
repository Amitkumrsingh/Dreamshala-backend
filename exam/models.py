# exam/models.py

from django.db import models

EXAM_FREQUENCY_CHOICES = [
    ('Once a year', 'Once a year'),
    ('Twice a year', 'Twice a year'),
    # Add more options as needed
]

EXAM_MODE_CHOICES = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    # Add more options as needed
]

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

EXAMS_CHOICES = [
    ('Exam 1', 'Exam 1'),
    ('Exam 2', 'Exam 2'),
    # Add more options as needed
]

REGISTRATION_MODE_CHOICES = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    # Add more options as needed
]

PAYMENT_MODES_CHOICES = [
    ('Credit Card', 'Credit Card'),
    ('Debit Card', 'Debit Card'),
    ('Net Banking', 'Net Banking'),
    # Add more options as needed
]

CATEGORY_CHOICES = [
    ('General', 'General'),
    ('OBC', 'OBC'),
    ('SC', 'SC'),
    ('ST', 'ST'),
    # Add more options as needed
]

NEWS_CATEGORY_CHOICES = [
    ('Very Important', 'Very Important'),
    ('Important', 'Important'),
    ('Medium Important', 'Medium Important'),
    ('Less Important', 'Less Important'),
    # Add more options as needed
]

MODE_CHOICES = [
    ('Online', 'Online'),
    ('Offline', 'Offline'),
    # Add more options as needed
]


class ExamStep1(models.Model):
     # Basic Details
    logo = models.ImageField(upload_to='exam/logos/', blank=True, null=True)
    short_description = models.TextField(max_length=200, blank=True, null=True)
    detailed_description = models.TextField(max_length=500, blank=True, null=True)
    exam_frequency = models.CharField(max_length=20, choices=EXAM_FREQUENCY_CHOICES, blank=True, null=True)
    exam_mode = models.CharField(max_length=20, choices=EXAM_MODE_CHOICES, blank=True, null=True)
    states_applicable = models.CharField(max_length=50, choices=STATE_CHOICES, blank=True, null=True)

    # Contact Details
    exam_official_website = models.URLField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    other_links = models.TextField(blank=True, null=True)  # You may need a separate model for links with + button

    # Brochure
    upload_brochure = models.FileField(upload_to='exam/brochures/', blank=True, null=True)
    brochure_description = models.TextField(max_length=500, blank=True, null=True)
    keywords_meta_tags = models.TextField(max_length=200, blank=True, null=True)
    brochure_links = models.TextField(blank=True, null=True)  # You may need a separate model for links with + button
    exams_who_can_refer = models.CharField(max_length=20, choices=EXAMS_CHOICES, blank=True, null=True)

    # Registration Details
    registration_website = models.URLField(blank=True, null=True)
    registration_mode = models.CharField(max_length=20, choices=REGISTRATION_MODE_CHOICES, blank=True, null=True)
    payment_modes = models.CharField(max_length=20, choices=PAYMENT_MODES_CHOICES, blank=True, null=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES ,blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)

    registration_fees = models.CharField(max_length=20, blank=True)



class ExamStep2(models.Model):
    news_post = models.TextField(max_length=5000,blank=True, null=True)
    news_category = models.CharField(max_length=20, choices=NEWS_CATEGORY_CHOICES,blank=True, null=True)

    # Important Dates
    registration_start_date = models.DateField(blank=True, null=True)
    registration_end_date = models.DateField(blank=True, null=True)
    admit_card_release_date = models.DateField(blank=True, null=True)
    result_date = models.DateField(blank=True, null=True)

    # Exam Dates
    exam_dates = models.DateField(null=True, blank=True, default=None, help_text="Click + button to add more exam dates")

class ExamStep3(models.Model):
    # Exam Pattern
    excel_file = models.FileField(upload_to='exam_patterns/', null=True, blank=True)
    pattern_degree_branch = models.CharField(max_length=50, null=True, blank=True)
    pattern_mode = models.CharField(max_length=20, choices=MODE_CHOICES, null=True, blank=True)
    pattern_duration = models.CharField(max_length=20, null=True, blank=True)
    pattern_questions = models.CharField(max_length=20, null=True, blank=True)
    pattern_total_marks = models.CharField(max_length=20, null=True, blank=True)
    pattern_subjects_sections = models.TextField(null=True, blank=True, help_text="Separated by comma")
    pattern_medium = models.TextField(null=True, blank=True, help_text="Separated by comma")
    pattern_type_of_questions = models.TextField(max_length=500, null=True, blank=True)
    pattern_marking_scheme = models.TextField(max_length=500, null=True, blank=True)

    # Study Material
    material_file = models.FileField(upload_to='study_material/', null=True, blank=True)
    material_description = models.TextField(max_length=500, null=True, blank=True)
    material_keywords = models.TextField(null=True, blank=True)
    material_category = models.CharField(max_length=50, null=True, blank=True)
    material_exam_ref = models.CharField(max_length=50, null=True, blank=True)
    material_links = models.TextField(null=True, blank=True, help_text="Separated by comma")

    # Previous Year Question Paper
    question_paper_files = models.FileField(upload_to='question_papers/', null=True, blank=True)
    question_paper_exam = models.CharField(max_length=50, null=True, blank=True)
    question_paper_year = models.CharField(max_length=20, null=True, blank=True)
    question_paper_date = models.DateField(null=True, blank=True)
    question_paper_mode = models.CharField(max_length=20, choices=MODE_CHOICES, null=True, blank=True)
    question_paper_description = models.TextField(max_length=500, null=True, blank=True)
    question_paper_links = models.TextField(null=True, blank=True, help_text="Separated by comma")
    #FAQ
    faq_question = models.TextField(blank=True, null=True)
    faq_answer = models.TextField(blank=True, null=True)