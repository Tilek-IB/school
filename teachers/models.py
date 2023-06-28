from django.db import models
# from pupils.models import Pupil
# Create your models here.

class Teacher(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    # surname = models.CharField(max_length=100)
    date_birth = models.DateField()


    