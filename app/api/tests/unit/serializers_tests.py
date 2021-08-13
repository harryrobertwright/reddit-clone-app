from django.test import TestCase

from api.serializers import UserSerializer


class TestUserSerializer(TestCase):
    def setUp(self):
        self.serializer = UserSerializer()
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(
            set(self.data.keys()),
            set(["username", "date_joined", "last_login", "avatar"]),
        )
