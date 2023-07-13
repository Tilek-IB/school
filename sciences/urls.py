from django.urls import path, include
from .views import ScienceForTeacherViewSet, ScienceForAdminViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'science-for-admin', ScienceForAdminViewSet, basename='scientists')

urlpatterns = [
    path('', include(router.urls)),
    path('science-for-teacher/', ScienceForTeacherViewSet.as_view({'get': 'list'}), name='science_for_teacher'),

]
