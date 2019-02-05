from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.views import View

User = get_user_model()

class Landing(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("/dashboard/overview")
        else:
            return render(request, 'landing.html', {"url": settings.DOMAIN_URL})

class UserPortfolio(View):
    def get(self, request, username):
        return render(request, 'portfolio.html', {})

class Login(View):
    def post(self, request):
        email_or_username = request.POST.get("email_or_username")
        password = request.POST.get("password")
        try:
            user_obj = User.objects.get(email=email_or_username)
            user = authenticate(request, username=user_obj.email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({
                    "status": "login_success",
                    "url": settings.DOMAIN_URL + "/dashboard/overview"
                })
            else:
                return JsonResponse({
                    "status": "login_error",
                    "message": "Email or password was incorrect."
                })
        except User.DoesNotExist:
            try:
                user_obj = User.objects.get(username=email_or_username)
                user = authenticate(request, username=user_obj.email, password=password)
                if user is not None:
                    login(request, user)
                    return JsonResponse({
                        "status": "login_success",
                        "url": settings.DOMAIN_URL + "/dashboard/overview"
                    })
                else:
                    return JsonResponse({
                        "status": "login_error",
                        "message": "Email or password was incorrect."
                    })
            except User.DoesNotExist:
                return JsonResponse({
                        "status": "login_error",
                        "message": "Email or password was incorrect."
                    })

class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You were logged out successfully.")
        return redirect("/")

class Dashboard(View):
    def get(self, request):
        pass