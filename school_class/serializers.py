from rest_framework import serializers

from pupils.serializers import PupilSerializer
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer
from user.serializers import UserSerializer
from .models import SchoolClass


class SchoolClassSerializerForAdmin(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = SchoolClass
        fields = ('id', 'number', 'letter', 'teacher',)

    def create(self, validated_data):
        teacher_id = self.context['request'].data.get('teacher')
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)
            school_class = SchoolClass.objects.create(teacher=teacher, **validated_data)
        else:
            school_class = SchoolClass.objects.create(**validated_data)
        return school_class

    def update(self, instance, validated_data):  # check teacher id
        teacher_id = self.context['request'].data.get('teacher')
        if teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)
            instance.teacher = teacher
        instance.number = validated_data.get('number', instance.number)
        instance.letter = validated_data.get('letter', instance.letter)
        instance.save()
        return instance


class SchoolClassSerializerForTeacher(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    pupils = PupilSerializer(many=True, read_only=True)

    class Meta:
        model = SchoolClass
        fields = ('id', 'number', 'letter', 'pupils', 'user',)
