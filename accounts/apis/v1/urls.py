from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path("api-key/create/", create_api_key, name="create_api_key"),
]
