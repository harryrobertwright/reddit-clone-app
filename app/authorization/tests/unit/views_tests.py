from django.test import TestCase

from authorization.views import LoginView, LoginRefreshView, RegisterView


class TestRegisterView(TestCase):
    def setUp(self):
        self.view = RegisterView()

    def test_queryset_belongs_to_user_model(self):
        self.assertEqual("User", self.view.queryset.model.__name__)

    def test_serializer_class_is_register_serializer(self):
        self.assertEqual(
            "RegisterSerializer", self.view.serializer_class.__name__
        )


class TestLoginView(TestCase):
    def setUp(self):
        self.view = LoginView()

    def test_serializer_class_is_login_serializer(self):
        self.assertEqual(
            "LoginSerializer", self.view.serializer_class.__name__
        )

    def test_permissions_classes_only_include_allowany(self):
        permissions_classes = self.view.permission_classes
        self.assertEqual(1, len(permissions_classes))
        self.assertEqual(
            "AllowAny", self.view.permission_classes[0].__name__
        )

    def test_expected_allowed_methods(self):
        self.assertEqual(["POST", "OPTIONS"], self.view.allowed_methods)


class TestLoginRefreshView(TestCase):
    def setUp(self):
        self.view = LoginRefreshView()

    def test_serializer_class_is_login_refresh_serializer(self):
        self.assertEqual(
            "LoginRefreshSerializer", self.view.serializer_class.__name__
        )

    def test_permissions_classes_only_include_isauthenicated(self):
        permissions_classes = self.view.permission_classes
        self.assertEqual(1, len(permissions_classes))
        self.assertEqual(
            "AllowAny", self.view.permission_classes[0].__name__
        )

    def test_expected_allowed_methods(self):
        self.assertEqual(["GET", "OPTIONS"], self.view.allowed_methods)

    def test_authentication_classes_only_includes_jwtauthentication(self):
        authentication_classes = self.view.authentication_classes
        self.assertEqual(1, len(authentication_classes))
        self.assertEqual(
            "JWTAuthentication", authentication_classes[0].__name__ 
        )
