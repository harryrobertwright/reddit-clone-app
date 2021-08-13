from django.urls import include, path

urlpatterns = [
    path("auth/", include("authorization.urls")),
    path("api/", include("api.urls")),
]
