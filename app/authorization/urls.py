from django.urls import path

from .views import LoginView, LoginRefreshView, RegisterView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),
    path("login/", LoginView.as_view(), name="auth_login"),
    path("login/refresh/", LoginRefreshView.as_view(), name="token_refresh"),
]
