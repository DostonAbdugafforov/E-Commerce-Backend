from rest_framework import serializers
from account.models import CustomUser
import re


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'password',
            'password_confirm',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'date_of_birth',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }

    def validate_password(self, value):
        """
        Password validation:
        - At least 8 characters
        - At least 1 uppercase letter (A-Z)
        - At least 1 lowercase letter (a-z)
        - At least 1 special character (!@#$%^&*(),.?":{}|<>)
        """
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )

        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter (A-Z)."
            )

        if not re.search(r'[a-z]', value):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter (a-z)."
            )

        if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=\[\]\\\/`~;]', value):
            raise serializers.ValidationError(
                "Password must contain at least one special character (!@#$%^&* etc.)."
            )

        return value

    def validate(self, attrs):
        """Check if passwords match"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({
                "password_confirm": "Password fields didn't match."
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        return CustomUser.objects.create_user(
            password=password,
            **validated_data
        )


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(required=True, help_text="Refresh token for logout")

    def validate_refresh(self, value):
        """Refresh token bo'sh emasligini tekshirish"""
        if not value or value.strip() == "":
            raise serializers.ValidationError("Refresh token cannot be empty")
        return value


class CustomUserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            'email',
            "first_name",
            "last_name",
            'phone_number',
            'date_of_birth',
            'role',
            "created_at",
        ]