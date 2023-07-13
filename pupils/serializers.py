from .models import Pupil
from rest_framework import serializers
from user.serializers import UserSerializer
from school_class.models import SchoolClass
from teachers.serializers import TeacherSerializer

class SchoolClassForPupilSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    class Meta:
        model = SchoolClass
        fields = 'id', 'letter', 'number' ,'teacher'

class PupilSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    school_class = SchoolClassForPupilSerializer(read_only=True)
    class Meta:
        model = Pupil
        fields = 'id', 'user', 'date_of_birth', 'school_class'

        read_only_fields = ('user', 'id')
