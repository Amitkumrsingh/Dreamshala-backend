# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('SU', 'Superuser'),
        ('CO', 'Company User'),
        ('CL', 'Client'),
        ('VI', 'Visitor'),
    )
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES)