from django.urls import path
from .views import RegisterView, LoginView, UserProfileView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = "users"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", UserProfileView.as_view(), name="user-profile"),
]
