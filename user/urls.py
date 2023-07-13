from django.urls import path
from rest_framework import routers

from .views import PupilRegisterView, EmailVerificationView, LoginApiView, GetUserView, TeacherRegisterView, \
    LogoutView, DeleteUserView, ChangePasswordView, AdminRegisterView

router = routers.DefaultRouter()

urlpatterns = [
    path('pupil-register/', PupilRegisterView.as_view()),
    path('teacher-register/', TeacherRegisterView.as_view()),
    path('admin-register/', AdminRegisterView.as_view()),
    path('get-user/', GetUserView.as_view()),
    path('email-verification/', EmailVerificationView.as_view()),
    path('login/', LoginApiView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('delete-user/', DeleteUserView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),

]
