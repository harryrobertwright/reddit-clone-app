from django.test import TestCase

from authorization.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="testusername", password="testpassword123"
        )

    def test_model_has_avatar_field(self):
        self.assertTrue(hasattr(self.user, "avatar"))

    def test_default_avatar_field_is_none(self):
        self.assertIsNone(self.user.avatar._file)
