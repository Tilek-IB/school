from rest_framework import serializers
from .models import New

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
        read_only_fields = ['writer'] # только для чтения

    def validate_title(self, value): # проверка на длину
        if len(value) < 5:
            raise serializers.ValidationError('Длина заголовка должна быть больше 10 символов')
        return value

