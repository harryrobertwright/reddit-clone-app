from django.test import Client, TestCase
from rest_framework.test import APIRequestFactory, APITestCase

from authorization.models import User
from authorization.views import LoginView, LoginRefreshView, RegisterView


class TestRegisterView(TestCase):
    def setUp(self):
        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
            "confirm_password": "testpassword123",
        }
        self.view = RegisterView()
        self.client = Client()

    def test_successful_user_registration(self):
        response = self.client.post("/auth/register/", self.user_attributes)
        self.assertEqual(200, response.status_code)
        self.assertEqual(
            {
                "message": "User successfully registered."
            },
            response.data,
        )

    def test_cannot_register_duplicate_user(self):
        self.client.post("/auth/register/", self.user_attributes)
        response = self.client.post("/auth/register/", self.user_attributes)
        self.assertEqual(400, response.status_code)
        self.assertEqual(
            {
                "email": ["This email is already in use."],
                "username": ["This username is already in use."],
            },
            response.data,
        )

    def test_cannot_register_with_non_matching_passwords(self):
        self.user_attributes["confirm_password"] = "nonmatching123"
        response = self.client.post("/auth/register/", self.user_attributes)
        self.assertEqual(400, response.status_code)
        self.assertEqual(
            {
                "password": ["Password fields didn't match."]
            },
            response.data,
        )


class TestLoginView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        User.objects.create_user(**self.user_attributes)

        self.view = LoginView()

    def test_login_success_with_valid_credentials(self):
        request = self.factory.post(
            "/auth/login/",
            {
                "username": self.user_attributes["username"],
                "password": self.user_attributes["password"],
            },
        )

        response = self.view.as_view()(request)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.data.get("access"))

    def test_successful_login_returns_refresh_token_cookie(self):
        request = self.factory.post(
            "/auth/login/",
            {
                "username": self.user_attributes["username"],
                "password": self.user_attributes["password"],
            },
        )

        response = self.view.as_view()(request)
        self.assertIsNotNone(response.cookies.get("refresh"))    

    def test_login_failure_with_invalid_credentials(self):
        request = self.factory.post(
            "/auth/login/",
            {
                "username": "nottherightusername",
                "password": "nottherightpassword123",
            },
        )

        response = self.view.as_view()(request)
        self.assertEqual(401, response.status_code)
        self.assertEqual(
            {
                "detail": "No active account found with the given credentials"
            },
            response.data,
        )


class TestLoginRefreshView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        User.objects.create_user(**self.user_attributes)

        self.view = LoginRefreshView()

        request = self.factory.post(
            "/auth/login/",
            {
                "username": self.user_attributes["username"],
                "password": self.user_attributes["password"],
            },
        )

        response = LoginView().as_view()(request)

        self.refresh_token = response.cookies.get("refresh").value

    def test_returns_new_access_token_when_valid_refresh_token_sent(self):
        request = self.factory.get("/auth/login/refresh/")
        request.COOKIES["refresh"] = self.refresh_token

        response = self.view.as_view()(request)

        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.data.get("access"))

    def test_returns_error_when_invalid_refresh_token_sent(self):
        request = self.factory.get("/auth/login/refresh/")
        request.COOKIES["refresh"] = "invalid_refresh_token"

        response = self.view.as_view()(request)

        self.assertEqual(401, response.status_code)
        self.assertEqual(
            {
                "detail": "Token is invalid or expired",
                "code": "token_not_valid"
            },
            response.data,
        )
