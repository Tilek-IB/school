from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Science
from .serializers import ScienceSerializer
from school_class.permissions import IsAdmin
from school_class.permissions import IsTeacher
from teachers.models import Teacher
from rest_framework import serializers

class ScienceForAdminViewSet(viewsets.ModelViewSet):
    queryset = Science.objects.all().prefetch_related('teacher')
    serializer_class = ScienceSerializer
    permission_classes = [IsAdmin]

    def update(self, request, *args, **kwargs): # use set and iterator
        teacher_id = request.data.get('teacher')
        if teacher_id is None:
            raise serializers.ValidationError('Teacher id not found')
        if not isinstance(teacher_id, list):
            raise serializers.ValidationError('Teacher id must be a list')
        teachers = Teacher.objects.filter(id__in=teacher_id)
        if teachers is None:
            raise serializers.ValidationError('Teacher not found')
        science = self.get_object()
        science.teacher.add(*teachers)
        return super().update(request, *args, **kwargs)

class ScienceForTeacherViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Science.objects.all()
    serializer_class = ScienceSerializer
    permission_classes = [IsTeacher]

