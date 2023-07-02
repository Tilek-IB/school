from django.db import models
# from teachers.models import Teacher
# Create your models here.

# from class.models import Class
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class Pupil(AbstractUser):
    date_of_birth = models.DateField()
    