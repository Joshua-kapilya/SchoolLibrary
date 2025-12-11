from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # check if user has admin role
            try:
                profile = user.userprofile
                if profile.role == "admin":
                    login(request, user)
                    return redirect("admin_dashboard")
                else:
                    messages.error(request, "You are not allowed to access the admin portal.")
            except UserProfile.DoesNotExist:
                messages.error(request, "Profile not found. Contact system administrator.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/admin_login.html")

def admin_dashboard(request):
    # protect admin dashboard
    if not request.user.is_authenticated:
        return redirect("admin_login")

    try:
        if request.user.userprofile.role != "admin":
            return redirect("admin_login")
    except:
        return redirect("admin_login")

    return render(request, "accounts/admin_dashboard.html")


# accounts/views.py
from django.shortcuts import redirect
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('home')  # redirect to homepage after logout

