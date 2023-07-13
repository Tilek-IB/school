from rest_framework import serializers

from user.models import User
from .models import New


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number']


class NewSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)

    class Meta:
        model = New
        fields = 'id', 'title', 'description', 'writer', 'for_teacher', 'created_at', 'updated_at'
        read_only_fields = ['writer']  # только для чтения

    def validate_title(self, value):  # проверка на длину
        if len(value) < 5:
            raise serializers.ValidationError('Длина заголовка должна быть больше 10 символов')
        return value
