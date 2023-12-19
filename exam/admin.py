# exam/admin.py

from django.contrib import admin
from .models import ExamStep1, ExamStep2, ExamStep3

@admin.register(ExamStep1)
class ExamStep1Admin(admin.ModelAdmin):
    list_display = ('id',)  # Add other fields as needed

@admin.register(ExamStep2)
class ExamStep2Admin(admin.ModelAdmin):
    list_display = ('id',)  # Add other fields as needed

@admin.register(ExamStep3)
class ExamStep3Admin(admin.ModelAdmin):
    list_display = ('id',)  # Add other fields as needed
