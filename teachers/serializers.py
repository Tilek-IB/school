from .models import Teacher
from rest_framework import serializers
from pupils.serializers import UserSerializer
from school_class.models import SchoolClass

class SchoolClassForTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = '__all__'
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    school_class = SchoolClassForTeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = 'id', 'user', 'school_class'


class TeacherRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', )