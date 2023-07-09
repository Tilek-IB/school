from rest_framework import permissions
from .models import SchoolClass


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_admin:
            return True
        return False


class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:  # is_staff - это is_teacher
            return True
        return False


class IsPupil(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_verified:
            return True
        return False


class IsPupilOfThisClass(permissions.BasePermission):  # проверяет, является ли пользователь учеником этого класса
    def has_permission(self, request, view):  # request.user - это ученик
        if not request.user.is_authenticated:
            return False
        if request.user.is_verified:
            return True
        return False
        if request.user.school_class == SchoolClass.objects.get(id=view.kwargs['pk']):  # если ученик этого класса
            return True
        return False
