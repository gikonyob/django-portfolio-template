from django.shortcuts import render
from django.views import View

class LandingPage(View):
    def get(self, request):
        return render(request, 'landing.html', {})

class UserPortfolio(View):
    def get(self, request, username):
        return render(request, 'portfolio.html', {})

class Login(View):
    def get(self, request):
        return render(request, 'login.html', {})
    def post(self, request):
        pass