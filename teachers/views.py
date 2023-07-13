from .models import Teacher
from rest_framework import viewsets
from .serializers import TeacherSerializer
from school_class.permissions import IsAdmin, IsTeacher
from school_class.models import SchoolClass
from rest_framework.response import Response
from rest_framework import status

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().select_related('user').prefetch_related('school_class')
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin | IsTeacher]

    def get_queryset(self):
        if self.request.user.is_admin:
            return Teacher.objects.all().select_related('user').prefetch_related('school_class')
        return Teacher.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def update(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_403_FORBIDDEN)





