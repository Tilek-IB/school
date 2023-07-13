from random import randint

from django.conf import settings
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from school_class.permissions import IsSuperuser
from user.models import User
from .serializers import EmailVerificationSerializer, PupilRegisterSerializer, TeacherRegisterSerializer
from .serializers import LoginSerializer, UserSerializer, GetUserSerializer, ChangePasswordSerializer, \
    AdminRegisterSerializer


def generate_verification_code():
    return randint(100000, 999999)


def send_verification_code(email, verification_code):
    send_mail(
        'Verification code',
        f'Your verification code is {verification_code}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )


class EmailVerificationView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = EmailVerificationSerializer

    def post(self, request):
        serializer = EmailVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, id=serializer.validated_data['id'])
        if user.is_verified:
            return Response({'message': 'User is already verified'}, status=400)
        if user.verification_code == serializer.validated_data['verification_code']:
            user.is_active = True
            user.is_verified = True
            user.verification_code = None
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'detail': 'Email verified successfully'}, status=200)
        return Response({'message': 'Wrong verification code'}, status=400)


class PupilRegisterView(generics.CreateAPIView):
    serializer_class = PupilRegisterSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pupil = serializer.save()
        user = pupil.user
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        confirmation_code = generate_verification_code()
        user.verification_code = confirmation_code
        user.save()

        send_verification_code(user.email, confirmation_code)

        return Response({'id': user.id, 'email': user.email,
                         'detail': 'Pupil created successfully, verification code sent to your email'},
                        status=status.HTTP_201_CREATED)


class TeacherRegisterView(generics.CreateAPIView):
    serializer_class = TeacherRegisterSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):  # Добавить проверку на существование связи с учеником
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        user = teacher.user
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        confirmation_code = generate_verification_code()
        user.verification_code = confirmation_code
        user.is_staff = True
        user.save()

        send_verification_code(user.email, confirmation_code)

        return Response({'id': user.id, 'email': user.email,
                         'detail': 'Teacher created successfully, verification code sent to your email'},
                        status=status.HTTP_201_CREATED)

class AdminRegisterView(generics.CreateAPIView):
    serializer_class = AdminRegisterSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        admin = serializer.save()
        user = admin.user
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        confirmation_code = generate_verification_code()
        user.verification_code = confirmation_code
        user.is_superuser = True
        user.save()

        send_verification_code(user.email, confirmation_code)

        return Response({'id': user.id, 'email': user.email,
                         'detail': 'Admin created successfully, verification code sent to your email'},
                        status=status.HTTP_201_CREATED)
class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'],
                            password=serializer.validated_data['password'])
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_verified:
            raise AuthenticationFailed('Your email is not verified')
        user.last_login = timezone.now()
        user.save()
        token = Token.objects.get_or_create(user=user)  # если токен уже существует, то он не создается
        data = {
            'email': user.email,
            'last_name': user.last_name,
            'token': token[0].key,
        }
        return Response(data=data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class GetUserView(generics.GenericAPIView):  # функция для получения данных о пользователе
    serializer_class = GetUserSerializer

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteUserView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def delete(self, request):
        request.user.delete()  # удаление пользователя
        return Response(status=status.HTTP_200_OK)


from django.contrib.auth.hashers import make_password


def set_password(password):
    return make_password(password)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsSuperuser]

    def post(self, request, *args, **kwargs):
        user = authenticate(email=request.user.email, password=request.data['old_password'])
        if user is None:
            return Response({'detail': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'Password changed  successfully'}, status=status.HTTP_200_OK)
