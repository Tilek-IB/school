from django.urls import path
from .main_views import index
from .user_views import PupilListView, PupilDetailView
from .news_views import NewsListView


urlpatterns = [
    path('', index, name='home'),
    path('pupils/', PupilListView.as_view(), name='pupil_list'),
    path('pupils/<int:pk>/', PupilDetailView.as_view(), name='pupil_detail'),
    path('news/', NewsListView.as_view(), name='news_list'),
]
