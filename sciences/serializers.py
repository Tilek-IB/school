from rest_framework import serializers

from teachers.serializers import TeacherSerializer
from .models import Science


class ScienceSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Science
        fields = '__all__'

    def create(self, validated_data):
        teacher = validated_data.pop('teacher')
        if teacher == list():
            raise serializers.ValidationError('Укажите 1 учителя')
        if not teacher:
            raise serializers.ValidationError('Укажите учителя')
        science = Science.objects.create(**validated_data)
        try:
            science.teacher.set(teacher)
        except:
            raise serializers.ValidationError('Укажите учителя')

        return science
    def update(self, instance, validated_data):
        teacher = validated_data.pop('teacher')
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        instance.teacher.set(teacher)