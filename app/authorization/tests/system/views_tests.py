from django.test import Client, TestCase

from authorization.views import RegisterView


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
            '{"message":"User successfully registered."}',
            response.content.decode("utf-8"),
        )

    def test_cannot_register_duplicate_user(self):
        self.client.post("/auth/register/", self.user_attributes)
        response = self.client.post("/auth/register/", self.user_attributes)
        self.assertEqual(400, response.status_code)
        self.assertEqual(
            {
                "email": ["This email is already in use."],
                "username": ["This username is already in use."]
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
