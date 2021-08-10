from django.test import TestCase
from rest_framework.serializers import ValidationError

from authorization.serializers import RegisterSerializer


class TestRegisterSerializer(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
            "confirm_password": "testpassword123",
        }

        self.serializer = RegisterSerializer()
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(
            set(self.data.keys()),
            set(["email", "username", "password", "confirm_password"]),
        )

    def test_successful_validation_returns_user_attributes(self):
        self.assertEqual(
            self.serializer.validate(attrs=self.user_attributes),
            self.user_attributes
        )

    def test_validation_of_non_matching_passwords(self):
        self.user_attributes["confirm_password"] = "nonmatchingpassword123"
        self.assertRaises(
            ValidationError,
            self.serializer.validate,
            attrs=self.user_attributes
        )
