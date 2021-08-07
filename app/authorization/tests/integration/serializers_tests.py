from django.test import TestCase

from authorization.models import User
from authorization.serializers import RegisterSerializer


class RegisterSerializerTest(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
            "confirm_password": "testpassword123",
        }

        self.serializer = RegisterSerializer()

    def test_successful_user_creation_returns_user_object(self):
        validated_data = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        self.assertIsInstance(self.serializer.create(validated_data), User)
