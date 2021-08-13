from django.test import TestCase

from authorization.models import User
from api.serializers import UserSerializer


class TestLoginSerializer(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        self.user = User.objects.create_user(**self.user_attributes)

        self.serializer = UserSerializer(instance=self.user)

    def test_serialized_user_returns_expected_data(self):
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
