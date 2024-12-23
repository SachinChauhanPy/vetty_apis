from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def LoginView(request):
    if request.method == "POST":
        # Get email and password from the POST request
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log in the user
            login(request, user)
            messages.success(request, "Logged in successfully.")
            # Redirect to api_key dashboard
            return redirect("crypto:dashboard")  
        else:
            messages.error(request, "Invalid email or password.")
    
    # Render the login page for GET requests
    return render(request, "accounts/login.html")

@login_required
def LogoutView(request):
    logout(request)
    return redirect("accounts:login")