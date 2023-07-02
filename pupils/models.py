from django.db import models
# from teachers.models import Teacher
# Create your models here.

# from class.models import Class
from django.contrib.auth.base_user import BaseUserManager

# class Pupil(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = 
#     last_name = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     date_birth = models.DateField()
    
#     date_joined = models.

#     is_pupil = models.BooleanField(default=True)




# class MyCustomUserManager(BaseUserManager):
#     def create_user(self, phone_number, password, **extra_fields):

#         if not phone_number:
#             raise ValueError('The phone number must be set')
#         user = self.model(phone_number=phone_number, **extra_fields)   # дает модельку 
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, phone_number, password, **extra_fields):

#         extra_fields.setdefault('is_staff', True)  # если такого назв нет до берет
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
            
#         return self.create_user(phone_number, password, **extra_fields)
    


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, unique=True)
#     date_birth = models.DateField(null=True, blank=True)
#     photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
#     phone_number = PhoneNumberField(null=False, blank=False, unique=True) 
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     chat_id = models.CharField(max_length=100, null=True, blank=True)
#     favorite = models.ManyToManyField(Hero)


#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS =  ['username', 'email']

#     objects = MyCustomUserManager()

#     def __str__(self) -> str:
#         return str(self.phone_number)

from django.contrib.auth.models import AbstractUser

class Pupil(AbstractUser):
    date_of_birth = models.DateField()
    