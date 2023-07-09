from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import SchoolClass
from .serializers import SchoolClassSerializer, SchoolClassForTeacherSerializer
from .permissions import IsAdmin, IsTeacher, IsPupil, IsPupilOfThisClass
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
class SchoolClassViewSet(viewsets.ModelViewSet): #
    serializer_class = SchoolClassSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        queryset = SchoolClass.objects.all().select_related('teacher')

        if self.request.user.is_staff:
            return queryset
        if self.request.user.is_admin:
            return queryset

        return queryset.filter(teacher=self.request.user) # если у пользователя есть атрибут teacher

class SchoolClassViewForTeacher(GenericViewSet, RetrieveModelMixin): # возможность просматривать классы, в которых он учит
    serializer_class = SchoolClassForTeacherSerializer
    permission_classes = [IsTeacher, IsAuthenticated]

    lookup_field = 'teacher' # по какому полю искать
    def get_queryset(self):
        queryset = SchoolClass.objects.all().select_related('teacher', 'pupil')

        if self.request.user.is_staff:
            return queryset
    def get_object(self): # возвращает класс, в котором учится учитель
        return self.request.user.teacher.school_class

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)











# def get_queryset(self):
#     queryset = Order.objects.all().select_related('driver', 'company', 'shipper', 'cargo_type'). \
#         prefetch_related('users')
#
#     if self.request.user.is_staff:
#         return queryset
#
#     if hasattr(self.request.user, 'shipper'): # если у пользователя есть атрибут shipper
#         shipper = self.request.user.shipper
#         return queryset.filter(shipper=shipper)
#
#     return queryset