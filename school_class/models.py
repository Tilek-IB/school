from django.db import models

# Create your models here.

from teachers.models import Teacher 


class Class(models.Model):
    number = models.IntegerField(max_length=10)
    letter = models.CharField(max_length=10)
    class_teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL, related_name='cool_pupils')
    
