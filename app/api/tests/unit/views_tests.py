from django.test import TestCase

from api.views import UserView


class TestUserView(TestCase):
    def setUp(self):
        self.view = UserView()

    def test_queryset_belongs_to_user_model(self):
        self.assertEqual("User", self.view.queryset.model.__name__)

    def test_serializer_class_is_user_serializer(self):
        self.assertEqual(
            "UserSerializer", self.view.serializer_class.__name__
        )

    def test_permissions_classes_only_include_isauthenicated(self):
        permissions_classes = self.view.permission_classes
        self.assertEqual(1, len(permissions_classes))
        self.assertEqual("IsAuthenticated", permissions_classes[0].__name__)

    def test_expected_allowed_methods(self):
        self.assertEqual(["GET", "OPTIONS"], self.view.allowed_methods)

    def test_authentication_classes_only_includes_jwtauthentication(self):
        authentication_classes = self.view.authentication_classes
        self.assertEqual(1, len(authentication_classes))
        self.assertEqual(
            "JWTAuthentication", authentication_classes[0].__name__ 
        )
