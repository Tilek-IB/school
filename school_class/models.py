from django.db import models

from teachers.models import Teacher


class SchoolClass(models.Model):
    number = models.IntegerField(null=True)
    letter = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL, related_name='school_class', blank=True)

    def __str__(self):
        return f'id {self.id} {self.number}{self.letter}'
