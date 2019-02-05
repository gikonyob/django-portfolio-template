from django.urls import path
from django.contrib.auth.decorators import login_required
import users.views as user_views

urlpatterns = [
    path('login', user_views.Login.as_view(), name='login'),
    path('logout', login_required(user_views.Logout.as_view(), login_url='landing'), name='logout'),
]