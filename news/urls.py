from django.urls import path, include
from .views import NewViewSet, NewForAllSchoolViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('new', NewViewSet, basename='new')

urlpatterns = [
    path('', include(router.urls)),
    path('news-all/', NewForAllSchoolViewSet.as_view({'get': 'list'})),

]
