from django.urls import path
from .views import LoginView,LogoutView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
]
