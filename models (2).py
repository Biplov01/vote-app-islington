
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(models.Model):
    age = models.IntegerField(null=True, blank=True)
    # Add other custom fields like age, address, etc.
