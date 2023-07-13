from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SchoolClassForAdminViewSet, SchoolClassForTeacherViewSet

router = DefaultRouter()
router.register('school-class-for-admin', SchoolClassForAdminViewSet, basename='school_class_for_admin')

urlpatterns = [
    path('', include(router.urls)),
    path('school-class-for-teacher/<int:pk>/', SchoolClassForTeacherViewSet.as_view({'get': 'retrieve'})),
    path('school-class-for-teacher/', SchoolClassForTeacherViewSet.as_view({'get': 'list'})),
]
