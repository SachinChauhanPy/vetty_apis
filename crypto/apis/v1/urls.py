from django.urls import path
from .views import *

app_name = "crypto"

urlpatterns = [
    path("coins/", coin_list_view, name="coin-list"),
    path("coins/categories/", coin_categories_view, name="coin-categories"),
    path("coins/<str:coin_id>/", specific_coin_view, name="specific-coin"),
    path("health/", check_gecko_api_health, name="health-check"),
]
