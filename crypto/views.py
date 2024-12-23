from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework_api_key.models import APIKey

# Create your views here.


@login_required
def APIDashboard(request):
    api_keys = APIKey.objects.all()
    context = {"title": "Vetty APIs", "api_keys": api_keys}
    return render(request, "crypto/dashboard.html", context)
