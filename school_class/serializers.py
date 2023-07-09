from rest_framework import serializers
from .models import SchoolClass

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ('id', 'number', 'letter', 'teacher', 'pupils')
        read_only_fields = ('id',)
        depth = 1   # определяет глубину вложенности для сериализации связанных объектов


class SchoolClassForTeacherSerializer(serializers.ModelSerializer):
    pupils = serializers.StringRelatedField(many=True) # позволяет выводить список учеников в виде списка их имен
    class Meta:
        model = SchoolClass
        fields = ('id', 'number', 'letter', 'teacher', 'pupils')
        read_only_fields = ('id',)
        depth = 1