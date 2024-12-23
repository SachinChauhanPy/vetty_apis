"""
URL configuration for vetty_apis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from decouple import config

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

current_api_version = config("API_VERSION", default="v1")

# Swagger schema view definition
schema_view = get_schema_view(
    openapi.Info(
        title="Crypto API",
        default_version="v1",
        description="API documentation for the Vetty APIs project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sachinchauhan19@outlook.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django Admin URLs
    path("admin/", admin.site.urls),
    # Accounts URLs
    path("accounts/", include("accounts.urls")),
    # Crypto App URLs
    path("", include("crypto.urls")),
    # Accounts APIs
    path(
        f"accounts/api/{current_api_version}/",
        include(f"accounts.apis.{current_api_version}.urls", "accounts_api"),
    ),
    # Crypto APIs
    path(
        f"crypto/api/{current_api_version}/",
        include(f"crypto.apis.{current_api_version}.urls", "crypto_api"),
    ),
    # Swagger URLs
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc",
         cache_timeout=0), name="schema-redoc"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
