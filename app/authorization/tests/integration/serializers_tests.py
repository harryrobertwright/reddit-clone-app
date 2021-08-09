from django.test import TestCase

from authorization.models import User
from authorization.serializers import RegisterSerializer


class TestRegisterSerializer(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
            "confirm_password": "testpassword123",
        }

        self.validated_data = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        self.serializer = RegisterSerializer()

    def test_successful_user_creation_returns_user_object(self):
        self.assertIsInstance(
            self.serializer.create(self.validated_data), User)

    def test_database_is_empty_on_test_initialisation(self):
        self.assertEqual(0, User.objects.all().count())
        self.serializer.create(self.validated_data)
        self.assertEqual(1, User.objects.all().count())
