from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        if "signup-form" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")
            # if passwords are not identical
            if password != password2:
                msg = "Please make sure passwords match!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            # if username already exists
            elif User.objects.filter(username=username).exists():
                msg = f"{username} already exists!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            # if email already in use
            elif User.objects.filter(email=email).exists():
                msg = f"{email} is already in use!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            # user valid
            else:
                User.objects.create_user(username, email, password)
                new_user = authenticate(username=username, password=password2)
                if new_user is not None:
                    login(request, new_user)
                    msg = f"Welcome, {username}!"
                    messages.success(request, msg)
                    return HttpResponseRedirect(request.path)
        elif "logout" in request.POST:
            msg = f"Logged out!"
            logout(request)
            messages.success(request, msg)
            return HttpResponseRedirect(request.path)
        elif "login-form" in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            new_login = authenticate(request, username=username, password=password)
            if new_login is None:
                msg = f"Incorrect credentials. Please retry login."
                messages.success(request, msg)
                return HttpResponseRedirect(request.path)
            else: 
                sec_code = str(random.randint(100000,999999))
                send_mail(
                    "PassItSafe: Your login code",
                    f"Your verification code is: {sec_code}.",
                    settings.EMAIL_HOST_USER,
                    [new_login.email],
                    fail_silently = False,
                )

    return render(request, "home.html")
