from django.test import TestCase

from authorization.models import User
from api.serializers import UserSerializer


class TestLoginSerializer(TestCase):
    def setUp(self):
        self.initial_user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        self.user = User.objects.create_user(**self.initial_user_attributes)

        self.serializer = UserSerializer(instance=self.user)

    def test_successful_validation_returns_user_attributes(self):
        full_user_attributes = User.objects.filter(id=self.user.id).values()[0]
        validated_data = self.serializer.validate(full_user_attributes)
        self.assertEqual(full_user_attributes, validated_data)

    def test_create_method_returns_expected_user_attributes(self):
        self.assertEqual(
            {
                "username": self.user.username,
                "date_joined": self.user.date_joined.isoformat().replace(
                    "+00:00", "Z"
                ),
                "last_login": self.user.last_login,
                "avatar": self.user.avatar,
            },
            self.serializer.data,
        )
