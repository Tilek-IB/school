from django.urls import path, include
from .views import ScienceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'scientists', ScienceViewSet, basename='scientists')

urlpatterns = [
    path('', include(router.urls)),
]
