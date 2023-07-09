from django.db import models

# Create your models here.

from teachers.models import Teacher 


class SchoolClass(models.Model):
    number = models.IntegerField(null=True)
    letter = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL, related_name='school_class', blank=True)


    def __str__(self):
        return f'{self.number}{self.letter}'
