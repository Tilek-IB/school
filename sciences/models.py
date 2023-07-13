from django.db import models
from teachers.models import Teacher

class Science(models.Model):
    name = models.CharField(max_length=255, unique=True)
    teacher = models.ManyToManyField(Teacher, related_name='sciences', blank=True)

    def __str__(self):
        return f'{self.name}'

