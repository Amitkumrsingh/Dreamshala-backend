# coaching/admin.py
from django.contrib import admin
from .models import CoachingStep1, CoachingStep2, CoachingStep3

@admin.register(CoachingStep1)
class CoachingStep1Admin(admin.ModelAdmin):
    list_display = ['logo', 'short_description', 'detailed_description', 'coaching_main_website']

@admin.register(CoachingStep2)
class CoachingStep2Admin(admin.ModelAdmin):
    list_display = ['management_name', 'management_role', 'management_email', 'management_contact']

@admin.register(CoachingStep3)
class CoachingStep3Admin(admin.ModelAdmin):
    list_display = ['coaching_name', 'coaching_gstin', 'year_of_establishment', 'pan_card_no', 'address_line_1', 'address_line_2', 'pincode']
