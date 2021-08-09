from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["email", "username", "password", "confirm_password"]
        extra_kwargs = {
            "username": {
                "validators": [UnicodeUsernameValidator()],
            },
            "email": {
                "validators": [EmailValidator()],
            },
        }

    def validate(self, attrs):
        if (
            User.objects.filter(username=attrs["username"]).exists()
            or User.objects.filter(email=attrs["email"]).exists()
        ):
            raise serializers.ValidationError(
                {"message": "This email/username is already in use."}
            )

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], email=validated_data["email"]
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
