from django.db import models
from django.conf import settings


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher')
    date_of_birth = models.DateField(null=True, blank=True)

    def create_superuser(self, email: str, password: str, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.is_superuser = True
        user.save()
        return user

    def __str__(self):
        return f'id {self.id} email {self.user.email}'
