# models.py in college app
from django.db import models

class CollegeStep1(models.Model):
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

    DAYS_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    name = models.CharField(max_length=15, blank=True, null=True)
    logo = models.ImageField(upload_to='college_logos/', blank=True, null=True)
    short_description = models.TextField(max_length=250, blank=True, null=True)
    detailed_description = models.TextField(max_length=500, blank=True, null=True)
    days_of_operation = models.ManyToManyField('WeekDay', blank=True)
    opens = models.TimeField(blank=True, null=True)
    closes = models.TimeField(blank=True, null=True)

    main_website = models.URLField(blank=True, null=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    other_links =  models.URLField(blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)
    instagram_account = models.URLField(blank=True, null=True)
    linkedin_page = models.URLField(blank=True, null=True)
    youtube_channel = models.URLField(blank=True, null=True)
    pinterest_account = models.URLField(blank=True, null=True)
    twitter_handle = models.URLField(blank=True, null=True)

    GSTIN = models.CharField(max_length=10, blank=True, null=True)
    establishment_year = models.PositiveIntegerField(blank=True, null=True)
    pan_card_number = models.CharField(max_length=10, blank=True, null=True)
    pan_card_upload = models.FileField(upload_to='pan_cards/', blank=True, null=True)
    address_line_1 = models.TextField(max_length=50, blank=True, null=True)
    address_line_2 = models.TextField(max_length=50, blank=True, null=True)
    landmark_locality = models.TextField(max_length=10, blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)


    # Management Contact
    management_name = models.CharField(max_length=15, blank=True, null=True)
    management_role = models.CharField(max_length=15, blank=True, null=True)
    management_email = models.EmailField(blank=True, null=True)
    management_contact = models.CharField(max_length=15, blank=True, null=True)


class WeekDay(models.Model):
    day = models.CharField(max_length=10, choices=CollegeStep1.DAYS_CHOICES,blank=True, null=True)




# class Location(models.Model):
#     state = models.CharField(max_length=50, choices=CollegeStep1.STATE_CHOICES, blank=True, null=True)
#     city = models.CharField(max_length=50, blank=True, null=True)
#     address_line_1 = models.TextField(max_length=50, blank=True, null=True)
#     address_line_2 = models.TextField(max_length=50, blank=True, null=True)
#     landmark_locality = models.TextField(max_length=10, blank=True, null=True)
#     pincode = models.PositiveIntegerField(blank=True, null=True)
#     branch_name = models.CharField(max_length=10, blank=True, null=True)
#     latitude = models.FloatField(blank=True, null=True)
#     longitude = models.FloatField(blank=True, null=True)


class CollegeStep2(models.Model):
    NEWS_CATEGORY_CHOICES = [
        ('very_imp', 'Very Important'),
        ('imp', 'Important'),
        ('medium_imp', 'Medium Important'),
        ('less_imp', 'Less Important'),
    ]

    DATE_DESCRIPTION_CHOICES = [
        ('description1', 'Description 1'),
        ('description2', 'Description 2'),
        # Add more descriptions as needed
    ]

    EVENT_DESCRIPTION_CHOICES = [
        ('description1', 'Description 1'),
        ('description2', 'Description 2'),
        # Add more descriptions as needed
    ]

    # Important News
    important_news = models.TextField(max_length=5000, blank=True, null=True)
    news_category = models.CharField(max_length=20, choices=NEWS_CATEGORY_CHOICES, blank=True, null=True)

    # Important Dates
    date_description = models.CharField(max_length=20, choices=DATE_DESCRIPTION_CHOICES, blank=True, null=True)
    starts_from = models.DateField(blank=True, null=True)
    ends_at = models.DateField(blank=True, null=True)
    event_description =models.CharField(max_length=20, choices=EVENT_DESCRIPTION_CHOICES, blank=True, null=True)



class CollegeStep3(models.Model):


    ENTRANCE_EXAM_CHOICES = [
        ('exam1', 'Exam 1'),
        ('exam2', 'Exam 2'),
        # Add more exams as needed
    ]

    COURSE_CHOICES = [
        ('course1', 'Course 1'),
        ('course2', 'Course 2'),
        # Add more courses as needed
    ]

    COURSE_DURATION_CHOICES = [
        ('duration1', 'Duration 1'),
        ('duration2', 'Duration 2'),
        # Add more durations as needed
    ]

    DEGREE_OFFERED_CHOICES = [
        ('degree1', 'Degree 1'),
        ('degree2', 'Degree 2'),
        # Add more degrees as needed
    ]

    FEES_CHOICES = [
        ('fees1', 'Fees 1'),
        ('fees2', 'Fees 2'),
        # Add more fees as needed
    ]

    MODE_CHOICES = [
        ('mode1', 'Mode 1'),
        ('mode2', 'Mode 2'),
        # Add more modes as needed
    ]

    ELIGIBILITY_CHOICES = [
        ('eligibility1', 'Eligibility 1'),
        ('eligibility2', 'Eligibility 2'),
        # Add more eligibility criteria as needed
    ]

    BATCH_STRENGTH_CHOICES = [
        ('strength1', 'Strength 1'),
        ('strength2', 'Strength 2'),
        # Add more batch strengths as needed
    ]

    CATEGORY_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        # Add more categories as needed
    ]

    SUBJECT_CHOICES = [
        ('subject1', 'Subject 1'),
        ('subject2', 'Subject 2'),
        # Add more subjects as needed
    ]

    DEGREE_BRANCH_CHOICES = [
        ('Degree1', 'Degree 1'),
        ('Degree2', 'Degree 2'),
        # Add more degree/branch choices as needed
    ]





    entrance_exams = models.ManyToManyField('EntranceExamChoice', blank=True)
    other_criteria = models.TextField(max_length=200, blank=True, null=True)

    course = models.CharField(max_length=20, choices=COURSE_CHOICES, blank=True, null=True)
    course_duration = models.CharField(max_length=20, choices=COURSE_DURATION_CHOICES, blank=True, null=True)
    degree_offered = models.CharField(max_length=20, choices=DEGREE_OFFERED_CHOICES, blank=True, null=True)
    course_description = models.TextField(max_length=500, blank=True, null=True)
    total_fees = models.CharField(max_length=20, choices=FEES_CHOICES, blank=True, null=True)
    course_mode = models.CharField(max_length=20, choices=MODE_CHOICES, blank=True, null=True)
    eligibility_criteria = models.CharField(max_length=20, choices=ELIGIBILITY_CHOICES, blank=True, null=True)
    batch_strength = models.CharField(max_length=20, choices=BATCH_STRENGTH_CHOICES, blank=True, null=True)

    degree_branch_application_process = models.CharField(max_length=20, choices=DEGREE_OFFERED_CHOICES, blank=True, null=True)
    application_process_description = models.TextField(max_length=500, blank=True, null=True)
    eligibility_criteria_description = models.TextField(max_length=500, blank=True, null=True)

    # previous cutoff
    degree_branch = models.CharField(max_length=20, choices=DEGREE_BRANCH_CHOICES, blank=True, null=True)
    parameter_of_cutoffs = models.TextField(max_length=500, blank=True, null=True)

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    percentile = models.CharField(max_length=5, blank=True, null=True)

    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, blank=True, null=True)
    subject_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    cutoff_percentile = models.CharField(max_length=5, blank=True, null=True)

class EntranceExamChoice(models.Model):
    choice = models.CharField(max_length=20, choices=CollegeStep3.ENTRANCE_EXAM_CHOICES, unique=True)

class CategoryPercentile(models.Model):
    college = models.ForeignKey(CollegeStep3, on_delete=models.CASCADE,blank=True, null=True)
    category = models.CharField(max_length=20, choices=CollegeStep3.CATEGORY_CHOICES,blank=True, null=True)
    percentile = models.CharField(max_length=5,blank=True, null=True)

class CollegeStep4(models.Model):
    DEGREE_CHOICES = [
        ('degree1', 'Degree 1'),
        ('degree2', 'Degree 2'),
        # Add more degrees as needed
    ]

    YEAR_OF_GRADUATION_CHOICES = [
        ('year1', 'Year 1'),
        ('year2', 'Year 2'),
        # Add more years as needed
    ]

    EXPERIENCE_CHOICES = [
        ('experience1', 'Experience 1'),
        ('experience2', 'Experience 2'),
        # Add more experiences as needed
    ]

    SPECIAL_CHOICES = [
        ('specialisation1', 'Specialisation 1'),
        ('specialisation2', 'Specialisation 2'),
        # Add more specialisations as needed
    ]
    BACKGROUND_CHOICES = [
        ('background1', 'Background 1'),
        ('background2', 'Background 2'),
        # Add more backgrounds as needed
    ]

    BASE_CITY_CHOICES = [
        ('city1', 'City 1'),
        ('city2', 'City 2'),
        # Add more cities as needed
    ]

    photo = models.ImageField(upload_to='people_photos/', blank=True, null=True)
    degree = models.CharField(max_length=20, choices=DEGREE_CHOICES, blank=True, null=True)
    year_of_graduation = models.CharField(max_length=20, choices=YEAR_OF_GRADUATION_CHOICES, blank=True, null=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True, null=True)
    latest_position_achievement = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True, null=True)
    links = models.TextField(max_length=10, blank=True, null=True)

    name = models.CharField(max_length=10,blank=True, null=True)
    specialisation = models.CharField(max_length=20, choices=SPECIAL_CHOICES, blank=True, null=True)
    background = models.CharField(max_length=20, choices=BACKGROUND_CHOICES, blank=True, null=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, blank=True, null=True)
    base_city = models.CharField(max_length=20, choices=BASE_CITY_CHOICES, blank=True, null=True)
    faculty_links = models.TextField(blank=True, null=True)


class CollegeStep5(models.Model):
    DEGREE_BRANCH_CHOICES = [
        ('degree1', 'Degree 1'),
        ('degree2', 'Degree 2'),
        # Add more degree choices as needed
    ]

    NUMBER_CHOICES = [
        ('number1', 'Number 1'),
        ('number2', 'Number 2'),
        # Add more number choices as needed
    ]



    FACILITY_CHOICES = [
        ('facility1', 'Facility 1'),
        ('facility2', 'Facility 2'),
        # Add more facility choices as needed
    ]

    UPLOAD_TYPE_CHOICES = [
        ('link', 'Link'),
        ('video/mp4', 'Video (MP4)'),
    ]

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    YEAR_CHOICES = [
        ('first_year', 'First Year'),
        ('second_year', 'Second Year'),
        ('third_year', 'Third Year'),
        ('fourth_year', 'Fourth Year'),
        # Add more year choices as needed
    ]

    COURSE_CHOICES = [
        ('course1', 'Course 1'),
        ('course2', 'Course 2'),
        # Add more course choices as needed
    ]


    degree_branch = models.CharField(max_length=20, choices=DEGREE_BRANCH_CHOICES, blank=True, null=True)
    overall_placement_description = models.TextField(max_length=500, blank=True, null=True)
    number_of_recruiters = models.CharField(max_length=20, choices=NUMBER_CHOICES, blank=True, null=True)
    number_of_offers = models.CharField(max_length=20, choices=NUMBER_CHOICES, blank=True, null=True)
    number_of_international_offers = models.CharField(max_length=20, choices=NUMBER_CHOICES, blank=True, null=True)
    to_recruiters = models.CharField(max_length=20, choices=NUMBER_CHOICES, blank=True, null=True)
    highest_package = models.CharField(max_length=20, choices=NUMBER_CHOICES, blank=True, null=True)
    average_package = models.CharField(max_length=20, choices=NUMBER_CHOICES, blank=True, null=True)

    #Photos

    image = models.ImageField(upload_to='additional_details/photos/', blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    category = models.ManyToManyField('PhotoCategory')
    keywords = models.TextField(max_length=200, blank=True, null=True)


    #Videos

    upload_type = models.CharField(max_length=20, choices=UPLOAD_TYPE_CHOICES,blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    video_file = models.FileField(upload_to='additional_details/videos/', blank=True, null=True)
    description = models.TextField(max_length=250, blank=True, null=True)
    keywords = models.TextField(max_length=200, blank=True, null=True)
    thumbnail = models.ImageField(upload_to='additional_details/videos/thumbnails/', blank=True, null=True)

    #Review

    name = models.CharField(max_length=10,blank=True, null=True)
    year_of_study = models.CharField(max_length=20, choices=YEAR_CHOICES,blank=True, null=True)
    course_taken = models.CharField(max_length=20, choices=COURSE_CHOICES,blank=True, null=True)
    overall_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    academics_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    faculty_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    infrastructure_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    accommodation_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    placement_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    social_life_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    detailed_description = models.TextField(max_length=500, blank=True, null=True)
    links = models.URLField(blank=True, null=True)
    photo_video = models.FileField(upload_to='additional_details/reviews/', blank=True, null=True)

    #Checklist
    available_facilities = models.ManyToManyField('Facility')
    students_in_batch = models.CharField(max_length=5, blank=True, null=True)
    total_students = models.CharField(max_length=5, blank=True, null=True)
    number_of_faculty = models.CharField(max_length=5, blank=True, null=True)

    #FAQ
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)



class PhotoCategory(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)

class Facility(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)



