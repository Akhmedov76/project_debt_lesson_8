from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app_users.models import UserModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(max_length=15, Validators=[
        UniqueValidator(queryset=UserModel.objects.all(), message='This phone number is already registered')
    ])

    class Meta:
        model = UserModel
        fields = ['username', 'phone_number', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_phone_number(self, phone_number: str):
        if not phone_number.startswith('+998'):
            raise serializers.ValidationError('Phone number should start with +')
        if not phone_number[4:].isdigit():
            raise serializers.ValidationError('Phone number should contain only digits')
        return phone_number

    def validate_password(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = UserModel.objects.create_user(**validated_data)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15, write_only=True)
    username = serializers.CharField(max_length=250)
