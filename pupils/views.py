from rest_framework import viewsets, filters

from .models import Pupil
from .serializers import PupilSerializer
from school_class.permissions import IsPupil
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as dj_filters
from school_class.permissions import IsAdmin
from rest_framework.response import Response
from rest_framework import status
class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all().select_related('school_class')
    serializer_class = PupilSerializer
    permission_classes = [IsPupil | IsAdmin]

    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('school_class',)
    ordering_fields = '__all__'
    search_fields = ('first_name', 'last_name', 'school_class__name')

    def get_queryset(self):
        if self.request.user.is_admin:
            return Pupil.objects.all().select_related('school_class')
        else:
            return Pupil.objects.filter(user=self.request.user).select_related('school_class')

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)