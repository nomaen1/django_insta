from django.urls import path
from .views import user, user_login, profile

urlpatterns = [
    path("register/", user, name="register"),
    path("login/", user_login, name="login"),
    path("profile/", profile, name="profile"),
]