from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from user.models import User
from pupils.models import Pupil
from teachers.models import Teacher
from user.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from school_class.models import SchoolClass
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'is_admin', 'is_verified', 'is_active', ]



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'password', ]
        extra_kwargs = {
            'password': {'write_only': True}    # password is not shown in response data
        }

    def create(self, validated_data):  # error anonymous user
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class EmailVerificationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    verification_code = serializers.CharField(max_length=6)

    def validate_code(self, value):
        if len(value) != 6 and not value.isdigit():
            raise ValidationError('Wrong verification code')
        return value

    def create(self, validated_data):
        user = get_object_or_404(User, id=validated_data['id'])
        if user.is_verified:
            raise ValidationError('User is already verified')
        if user.verification_code == validated_data['verification_code']:
            user.is_active = True
            user.is_verified = True
            user.save()
            return user
        raise ValidationError('Wrong verification code')


class PupilRegisterSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Pupil
        fields = ['user', 'date_of_birth', ]
        extra_kwargs = {
        'user': {'write_only': True} # на
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegisterSerializer.create(UserRegisterSerializer(), validated_data=user_data)
        pupil, created = Pupil.objects.update_or_create(user=user, **validated_data)
        return pupil


class TeacherRegisterSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'date_of_birth', ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegisterSerializer.create(UserRegisterSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(user=user, **validated_data)
        return teacher

class AdminRegisterSerializer(serializers.ModelSerializer):
    user = UserRegisterSerializer()

    class Meta:
        model = Teacher
        fields = ['user', 'date_of_birth', ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserRegisterSerializer.create(UserRegisterSerializer(), validated_data=user_data)
        user.is_admin = True
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

class ChangePasswordSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is not correct')
        return value

    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError('Passwords do not match')
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance
    def create(self, validated_data):
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetSchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = '__all__'
class GetPupilSerializer(serializers.ModelSerializer):
    school_class = GetSchoolClassSerializer()
    class Meta:
        model = Pupil
        fields = 'id', 'date_of_birth', 'school_class',

class GetTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = 'date_of_birth',


class GetUserSerializer(serializers.ModelSerializer):
    pupil = GetPupilSerializer()
    teacher = GetTeacherSerializer()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number', 'pupil', 'teacher', 'is_admin', 'is_staff', 'is_active', ]
