from rest_framework import serializers

from teachers.serializers import TeacherSerializer
from .models import Science
from teachers.models import Teacher

class ScienceSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=True, read_only=True)
    class Meta:
        model = Science
        fields = 'id', 'name', 'teacher'



class ScienceForTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = '__all__'



