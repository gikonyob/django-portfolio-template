from django.urls import path
from django.contrib.auth.decorators import login_required
import users.views as user_views

urlpatterns = [
    path('register', user_views.RegisterUser.as_view(), name='register_user'),
    path('logout', login_required(user_views.LogoutUser.as_view(), login_url='landing_page'), name='logout_user'),
]