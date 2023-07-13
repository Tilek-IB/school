from django.urls import path, include
from rest_framework import routers
from .views import PupilViewSet

router = routers.DefaultRouter()
router.register(r'pupil', PupilViewSet)


urlpatterns = [
    path('', include(router.urls)),
]