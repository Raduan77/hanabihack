from django.urls import path
from django.views.generic import RedirectView

from rest_framework.authtoken import views as auth_views

from . import views

api_urls = [
    path("api/v1/token", auth_views.obtain_auth_token, name="api-token-auth"),
    path("api/v1/login", views.LoginView.as_view(), name="api-login"),
]

urlpatterns = api_urls
