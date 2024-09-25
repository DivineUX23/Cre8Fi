from django.urls import path
from .views import UserRegistrationView  # SuperUserRegistrationView
from .views import FollowUserView, UnfollowUserView #CustomAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="user-register"),
    path("follow/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/", UnfollowUserView.as_view(), name="unfollow-user"),
    # path("login/", CustomAuthToken.as_view(), name="api_login"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
