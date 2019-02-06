from django.urls import path
from django.contrib.auth.decorators import login_required
import users.views as user_views

urlpatterns = [
    path('login', user_views.Login.as_view(), name='login'),
    path('logout', login_required(user_views.Logout.as_view(), login_url='landing'), name='logout'),
    path('dashboard/overview', login_required(user_views.Dashboard.as_view(), login_url='landing'), name='dashboard_home'),
    path('dashboard/skills', login_required(user_views.Skills.as_view(), login_url='landing'), name='dashboard_skills'),
    path('dashboard/quotes', login_required(user_views.Quotes.as_view(), login_url='landing'), name='dashboard_quotes'),
    path('dashboard/projects', login_required(user_views.Projects.as_view(), login_url='landing'), name='dashboard_projects'),
    path('dashboard/interests', login_required(user_views.Interests.as_view(), login_url='landing'), name='dashboard_interests'),
    path('dashboard/fun_facts', login_required(user_views.FunFacts.as_view(), login_url='landing'), name='dashboard_fun_facts'),
    path('dashboard/repositories', login_required(user_views.Repositories.as_view(), login_url='landing'), name='dashboard_repositories'),
    path('dashboard/socials', login_required(user_views.Socials.as_view(), login_url='landing'), name='dashboard_socials'),
    path('dashboard/articles', login_required(user_views.Articles.as_view(), login_url='landing'), name='dashboard_articles'),
]