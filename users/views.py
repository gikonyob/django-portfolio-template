from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
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
        return render(request, 'dashboard.html', {"page": "home"})

class Skills(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        skills = user.profile.skills.all()
        return render(request, 'dashboard.html', {"page": "skills", "skills": skills})

class Quotes(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        quotes = user.profile.quotes.all()
        return render(request, 'dashboard.html', {"page": "quotes", "quotes": quotes})

class Projects(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        projects = user.profile.projects.all()
        return render(request, 'dashboard.html', {"page": "projects", "projects": projects})

class Interests(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        interests = user.profile.interests.all()
        return render(request, 'dashboard.html', {"page": "interests", "interests": interests})

class FunFacts(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        fun_facts = user.profile.fun_facts.all()
        return render(request, 'dashboard.html', {"page": "fun_facts", "fun_facts": fun_facts})

class Repositories(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        repositories = user.profile.repositories.all()
        return render(request, 'dashboard.html', {"page": "repositories", "repositories": repositories})

class Socials(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        socials = user.profile.socials.all()
        return render(request, 'dashboard.html', {"page": "socials", "socials": socials})

class Articles(View):
    def get(self, request):
        email = request.user
        user = User.objects.get(email=email)
        articles = user.profile.articles.all()
        return render(request, 'dashboard.html', {"page": "articles", "articles": articles})