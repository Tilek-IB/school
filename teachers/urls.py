from rest_framework import routers
from django.urls import path, include
from .views import TeacherViewSet

router = routers.DefaultRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),
]