from django.test import TestCase

from api.serializers import UserSerializer
from authorization.models import User


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "avatar": None,
        }

        self.user = User.objects.create(
            username="testusername",
            email="test@email.com",
            password="testpassword123"
        )

        self.serializer = UserSerializer(instance=self.user)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(
            set(self.data.keys()), set(["id", "username", "email", "avatar"])
        )

    def test_username_field_content(self):
        self.assertEqual(self.data["username"],
                         self.user_attributes["username"])

    def test_email_field_content(self):
        self.assertEqual(self.data["email"], self.user_attributes["email"])

    def test_avatar_field_content(self):
        self.assertEqual(self.data["avatar"], self.user_attributes["avatar"])
