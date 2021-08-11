from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from authorization.models import User
from authorization.serializers import LoginSerializer, RegisterSerializer


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
            self.serializer.create(self.validated_data), User
        )

    def test_database_is_empty_on_test_initialisation(self):
        self.assertEqual(0, User.objects.all().count())
        self.serializer.create(self.validated_data)
        self.assertEqual(1, User.objects.all().count())


class TestLoginSerializer(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        self.user = User.objects.create_user(**self.user_attributes)

        self.serializer = LoginSerializer()
        self.returned_token = self.serializer.get_token(self.user)

    def test_get_token_method_returns_instance_of_token(self):
        self.assertIsInstance(self.returned_token, RefreshToken)

    def test_username_stored_in_returned_token_matches_users_username(self):
        self.assertEqual(
            self.user.username, self.returned_token["username"]
        )
