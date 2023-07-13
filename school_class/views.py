from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from .models import SchoolClass
from teachers.models import Teacher
from .permissions import IsAdmin, IsTeacher, IsPupil
from .serializers import SchoolClassSerializerForAdmin, SchoolClassSerializerForTeacher
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

class SchoolClassForAdminViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all().select_related('teacher', )
    serializer_class = SchoolClassSerializerForAdmin
    permission_classes = [IsAdmin]


class SchoolClassForTeacherViewSet(GenericViewSet, RetrieveModelMixin,ListModelMixin):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializerForTeacher
    permission_classes = [IsTeacher]

    def get_queryset(self):
        teacher = Teacher.objects.get(user=self.request.user)
        return SchoolClass.objects.filter(teacher=teacher)
    def retrieve(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(user=self.request.user)
        school_class = SchoolClass.objects.filter(teacher=teacher, id=kwargs['pk'])
        serializer = SchoolClassSerializerForTeacher(school_class, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        teacher = Teacher.objects.get(user=self.request.user)
        school_class = SchoolClass.objects.filter(teacher=teacher)
        serializer = SchoolClassSerializerForTeacher(school_class, many=True)
        return Response(serializer.data)
