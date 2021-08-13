from rest_framework.test import APIRequestFactory, APITestCase

from api.views import UserView
from authorization.models import User
from authorization.views import LoginView


class TestUserView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        self.user_attributes = {
            "username": "testusername",
            "email": "test@email.com",
            "password": "testpassword123",
        }

        self.user = User.objects.create_user(**self.user_attributes)

        request = self.factory.post(
            "/auth/login/",
            {
                "username": self.user_attributes["username"],
                "password": self.user_attributes["password"],
            },
        )

        self.response = LoginView().as_view()(request)

        self.access_token = self.response.data.get("access")

        self.view = UserView()

    def test_is_successful_given_valid_bearer_token(self):
        request = self.factory.get(
            "/api/profile/", HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )

        response = self.view.as_view()(request)

        self.assertEqual(200, response.status_code)

    def test_returns_error_given_invalid_bearer_token(self):
        request = self.factory.get(
            "/api/profile/", HTTP_AUTHORIZATION="Bearer invalidaccesstoken"
        )

        response = self.view.as_view()(request)

        self.assertEqual(401, response.status_code)
        self.assertEqual(
            {
                "detail": "Given token not valid for any token type",
                "code": "token_not_valid",
                "messages": [
                    {
                        "token_class": "AccessToken",
                        "token_type": "access",
                        "message": "Token is invalid or expired",
                    }
                ],
            },
            response.data,
        )
