# coaching/admin.py
# college/admin.py
from django.contrib import admin
from .models import CollegeStep1, CollegeStep2, CollegeStep3, CollegeStep4, CollegeStep5

@admin.register(CollegeStep1)
class CollegeStep1Admin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'main_website', 'contact_number', 'email', 'GSTIN', 'establishment_year', 'state', 'city')


@admin.register(CollegeStep2)
class CollegeStep2Admin(admin.ModelAdmin):
    list_display = ('id',)

@admin.register(CollegeStep3)
class CollegeStep3Admin(admin.ModelAdmin):
    list_display = ('id',)  # Add other fields as needed

@admin.register(CollegeStep4)
class CollegeStep4Admin(admin.ModelAdmin):
    list_display = ('id',)  # Add other fields as needed

@admin.register(CollegeStep5)
class CollegeStep5Admin(admin.ModelAdmin):
    list_display = ('id',)  # Add other fields as needed
