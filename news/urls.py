from django.urls import path, include
from .views import NewForAllSchoolViewSet, NewForAdminViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('new-for-admin', NewForAdminViewSet, basename='new')

urlpatterns = [
    path('', include(router.urls)),
    path('get-news/', NewForAllSchoolViewSet.as_view({'get': 'list'})),

]
