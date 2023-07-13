from typing import Any

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import get_object_or_404
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields) -> Any:
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_verified = True

        user.save(using=self._db)

        return user

    def delete_user(self, email):
        user = get_object_or_404(User, email=email)
        user.delete()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    photo = models.ImageField(upload_to='avatars/', blank=True, null=True)
    username = None
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    is_superuser = models.BooleanField(default=False)  # в школе это админ
    is_admin = models.BooleanField(default=False)  # в школе это учитель
    is_staff = models.BooleanField(default=False)  # определяет, может ли пользователь войти в админку
    is_active = models.BooleanField(default=False)  # определяет, активен ли пользователь
    is_verified = models.BooleanField(default=False)

    verification_code = models.CharField(max_length=6, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', ]

    def __str__(self):
        return f'id {self.id} email {self.email}'
