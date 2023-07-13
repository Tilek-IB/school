from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import New
from .serializers import NewSerializer
from school_class.permissions import IsAdmin
from rest_framework import mixins
from school_class.permissions import IsAdmin


class NewForAdminViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [IsAdmin]

    def perform_create(self, serializer):  # проверить что пользователь создает от своего имени
        serializer.save(writer=self.request.user)  # сохранить в поле writer текущего пользователя


class NewForAllSchoolViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return New.objects.filter(for_teacher=True)
        return New.objects.filter(for_teacher=False)