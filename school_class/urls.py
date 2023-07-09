from django.urls import path, include
from .views import SchoolClassViewSet, SchoolClassViewForTeacher
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('school_class', SchoolClassViewSet, basename='school_class')

urlpatterns = [
    path('', include(router.urls)),
    path('school_class_for_teacher/', SchoolClassViewForTeacher.as_view({'get': 'retrieve'})),
    ]