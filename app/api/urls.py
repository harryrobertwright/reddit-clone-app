from django.urls import path

from .views import UserView


urlpatterns = [
    path("profile/", UserView.as_view(), name="user_profile"),
]
