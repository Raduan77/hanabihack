from django.urls import path
from django.views.generic import RedirectView

from rest_framework.authtoken import views as auth_views

from . import views

api_urls = [
    path("api/v1/token", auth_views.obtain_auth_token, name="api-token-auth"),
    path("api/v1/login", views.LoginView.as_view(), name="api-login"),
    path(
        "api/v1/language/list",
        views.LanguageListAPIView.as_view(),
        name="language-list",
    ),
    path(
        "api/v1/language/<int:pk>/leaderboard",
        views.LeaderBoardAPIView.as_view(),
        name="language-leaderboard",
    ),
    path(
        "api/v1/language/<int:pk>/find-session",
        views.GetOrCreateSessionAPIView.as_view(),
        name="find-session",
    ),
    path(
        "api/v1/session/<int:pk>/check",
        views.CheckSessionAPIView.as_view(),
        name="check-session",
    ),
]

urlpatterns = api_urls
