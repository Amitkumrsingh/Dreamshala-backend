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



    logo = models.ImageField(upload_to='college_logos/', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)
    days_of_operation = models.CharField( blank=True, null=True)
    opens = models.TimeField(blank=True, null=True)
    closes = models.TimeField(blank=True, null=True)

    #CONTACT DETAILS

    main_website = models.TextField(blank=True, null=True)
    contact_number = models.CharField( blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    other_links =  models.TextField(blank=True, null=True)
    facebook_page = models.TextField(blank=True, null=True)
    instagram_account = models.TextField(blank=True, null=True)
    linkedin_page = models.TextField(blank=True, null=True)
    youtube_channel = models.TextField(blank=True, null=True)
    pinterest_account = models.TextField(blank=True, null=True)
    twitter_handle = models.TextField(blank=True, null=True)


   #College details(OFFICE)
    college_name = models.CharField( blank=True, null=True)
    GSTIN = models.CharField( blank=True, null=True)
    establishment_year = models.PositiveIntegerField(blank=True, null=True)

  #College Registered Address
    college_address_line_1 = models.TextField(blank=True, null=True)
    college_address_line_2 = models.TextField(blank=True, null=True)
    college_landmark_locality = models.TextField( blank=True, null=True)
    college_pincode = models.PositiveIntegerField(blank=True, null=True)
    college_state = models.CharField(choices=STATE_CHOICES, blank=True, null=True)
    college_city = models.CharField(blank=True, null=True)
    college_latitude = models.FloatField(blank=True, null=True)
    college_longitude = models.FloatField(blank=True, null=True)
    college_pan_card_number = models.CharField( blank=True, null=True)
    college_pan_card_upload = models.FileField(upload_to='pan_cards/', blank=True, null=True)

  #Location
    state = models.CharField(choices=STATE_CHOICES, blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    address_line_1 = models.TextField(blank=True, null=True)
    address_line_2 = models.TextField(blank=True, null=True)
    landmark_locality = models.TextField( blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.CharField(choices=STATE_CHOICES, blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    branch_name = models.CharField( blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)


    # Management Contact
    management_name = models.CharField( blank=True, null=True)
    management_role = models.CharField( blank=True, null=True)
    management_email = models.EmailField(blank=True, null=True)
    management_contact = models.CharField( blank=True, null=True)







# class Location(models.Model):
#     state = models.CharField(choices=CollegeStep1.STATE_CHOICES, blank=True, null=True)
#     city = models.CharField(blank=True, null=True)
#     address_line_1 = models.TextField(blank=True, null=True)
#     address_line_2 = models.TextField(blank=True, null=True)
#     landmark_locality = models.TextField( blank=True, null=True)
#     pincode = models.PositiveIntegerField(blank=True, null=True)
#     branch_name = models.CharField( blank=True, null=True)
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
    important_news = models.TextField(blank=True, null=True)
    news_category = models.CharField(choices=NEWS_CATEGORY_CHOICES, blank=True, null=True)

    # Important Dates
    date_description = models.TextField( blank=True, null=True)
    starts_from = models.TextField(blank=True, null=True)
    ends_at = models.TextField(blank=True, null=True)
    event_description =models.CharField(choices=EVENT_DESCRIPTION_CHOICES, blank=True, null=True)



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
        ('online', 'Online'),
        ('offline', 'Offline'),
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
        ('General', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
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





    entrance_exams = models.TextField(blank=True, null= True)
    other_criteria = models.TextField( blank=True, null=True)

    course = models.TextField(choices=COURSE_CHOICES, blank=True, null=True)
    course_duration = models.CharField(choices=COURSE_DURATION_CHOICES, blank=True, null=True)
    degree_offered = models.TextField( blank=True, null=True)
    course_description = models.TextField(blank=True, null=True)
    total_fees = models.CharField(choices=FEES_CHOICES, blank=True, null=True)
    course_mode = models.CharField(choices=MODE_CHOICES, blank=True, null=True)
    eligibility_criteria = models.CharField(choices=ELIGIBILITY_CHOICES, blank=True, null=True)
    batch_strength = models.TextField(blank=True, null=True)

    degree_branch_application_process = models.TextField(blank=True, null=True)
    application_process_description = models.TextField(blank=True, null=True)
    eligibility_criteria_description = models.TextField(blank=True, null=True)

    # previous cutoff
    degree_branch = models.TextField(blank=True, null=True)
    parameter_of_cutoffs = models.TextField(blank=True, null=True)

    category = models.CharField(choices=CATEGORY_CHOICES, blank=True, null=True)
    percentile = models.CharField( blank=True, null=True)

    subject = models.TextField(blank=True, null=True)
    subject_category = models.CharField(choices=CATEGORY_CHOICES, blank=True, null=True)
    cutoff_percentile = models.CharField( blank=True, null=True)

class EntranceExamChoice(models.Model):
    choice = models.CharField(choices=CollegeStep3.ENTRANCE_EXAM_CHOICES, unique=True)

class CategoryPercentile(models.Model):
    college = models.ForeignKey(CollegeStep3, on_delete=models.CASCADE,blank=True, null=True)
    category = models.CharField(choices=CollegeStep3.CATEGORY_CHOICES,blank=True, null=True)
    percentile = models.CharField(blank=True, null=True)

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
    degree = models.TextField( blank=True, null=True)
    year_of_graduation = models.TextField( blank=True, null=True)
    experience = models.TextField( blank=True, null=True)
    latest_position_achievement = models.TextField(blank=True, null=True)
    links = models.TextField( blank=True, null=True)
    name = models.TextField(blank=True, null=True)


      # Faculties
    faculty_photo = models.ImageField(upload_to='faculty_photos/',blank=True, null=True)
    faculty_name = models.CharField( blank=True, null=True)
    specialization = models.CharField( choices=[('spec1', 'Specialization 1'), ('spec2', 'Specialization 2')],blank=True, null=True)
    background = models.CharField( choices=[('bg1', 'Background 1'), ('bg2', 'Background 2')],blank=True, null=True)
    experience = models.CharField( choices=[('exp1', 'Experience 1'), ('exp2', 'Experience 2')],blank=True, null=True)
    base_city_faculty = models.CharField( choices=[('city1', 'City 1'), ('city2', 'City 2')],blank=True, null=True)
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

    excel_file = models.FileField(upload_to='placement_details_exel/', null=True, blank=True)
    degree_branch = models.TextField( blank=True, null=True)
    overall_placement_description = models.TextField(blank=True, null=True)
    number_of_recruiters = models.TextField( blank=True, null=True)
    number_of_offers = models.TextField( blank=True, null=True)
    number_of_international_offers = models.TextField( blank=True, null=True)
    to_recruiters = models.TextField( blank=True, null=True)
    highest_package = models.TextField( blank=True, null=True)
    average_package = models.TextField( blank=True, null=True)

    #Photos

    photo = models.ImageField(upload_to='additional_details/photos/', blank=True, null=True)
    photo_description = models.TextField(blank=True, null=True)
    photo_category = models.CharField(blank=True, null=True)
    photo_keywords_meta_tags = models.TextField( blank=True, null=True)


    #Videos


    video_link = models.TextField(blank=True, null=True)
    video_file = models.FileField(upload_to='additional_details/videos/', blank=True, null=True)
    video_description = models.TextField(blank=True, null=True)
    video_keywords_meta_tags = models.TextField( blank=True, null=True)
    video_thumbnail = models.ImageField(upload_to='additional_details/videos/thumbnails/', blank=True, null=True)

    #Review

    name = models.CharField(blank=True, null=True)
    year_of_study = models.CharField(blank=True, null=True)
    course_taken = models.TextField(blank=True, null=True)
    overall_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    academics_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    faculty_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    infrastructure_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    accommodation_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    placement_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    social_life_rating = models.IntegerField(choices=RATING_CHOICES,blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    photo_video = models.FileField(upload_to='additional_details/reviews/', blank=True, null=True)

    #Checklist
    available_facilities = models.CharField(blank=True, null=True)
    students_in_batch = models.CharField( blank=True, null=True)
    total_students = models.CharField( blank=True, null=True)
    number_of_faculty = models.CharField( blank=True, null=True)

    #FAQ
    faq_question = models.TextField(blank=True, null=True)
    faq_answer = models.TextField(blank=True, null=True)









