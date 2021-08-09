from django.test import TestCase

from authorization.views import RegisterView


class TestRegisterView(TestCase):
    def setUp(self):
        self.view = RegisterView()

    def test_queryset_belongs_to_user_model(self):
        self.assertEqual("User", self.view.queryset.model.__name__)

    def test_serializer_class_is_register_serializer(self):
        self.assertEqual("RegisterSerializer",
                         self.view.serializer_class.__name__)
