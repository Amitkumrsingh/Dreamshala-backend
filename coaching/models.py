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

class Facility(models.Model):
    name = models.CharField(blank=True, null=True)

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
    email = models.EmailField(blank=True, null=True)
    # Contact Number
    contact_number = models.CharField(blank=True, null=True)

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

    # Management Contact
    management_name = models.CharField(blank=True, null=True)
    management_role = models.CharField(blank=True, null=True)
    management_email = models.EmailField(blank=True, null=True)
    management_contact = models.CharField(blank=True, null=True)
    # ... add other fields for step 2

class CoachingStep3(models.Model):
    coaching_step2 = models.OneToOneField(CoachingStep2, on_delete=models.CASCADE, primary_key=True)

    # Coaching Details
    coaching_name = models.CharField(blank=True, null=True)
    coaching_gstin = models.CharField(blank=True, null=True)
    year_of_establishment = models.PositiveIntegerField(blank=True, null=True)
    pan_card_no = models.CharField(blank=True, null=True)
    upload_pan_card = models.FileField(upload_to='coaching_pan_cards/', blank=True, null=True)
    address_line_1 = models.TextField(blank=True, null=True)
    address_line_2 = models.TextField(blank=True, null=True)
    landmark_locality = models.CharField(blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='coaching_state', blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    location_latitude = models.FloatField(blank=True, null=True)
    location_longitude = models.FloatField(blank=True, null=True)
    # ... add other fields for step 3

