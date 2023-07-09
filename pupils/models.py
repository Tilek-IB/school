# from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from django.db import models

from school_class import models as school_class_models


class Pupil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pupil')
    date_of_birth = models.DateField(null=True, blank=True)
    school_class = models.ForeignKey(school_class_models.SchoolClass, null=True, on_delete=models.SET_NULL,
                                     related_name='pupils')  # set null если класс удалить то ученики останутся

    def __str__(self):
        return self.user.first_name

    def create_superuser(self, email: str, password: str, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.save()
        return user

    def create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def __str__(self):
        return self.user.email
