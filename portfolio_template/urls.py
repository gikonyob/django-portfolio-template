"""portfolio_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from portfolio import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^create_portfolio$', views.create_portfolio, name='create_portfolio'),
    url(r'^insert_to_database$', views.insert_to_database, name='insert_to_database'),
    url(r'^about$', views.about_me, name='about_me'),
    url(r'^profile$', views.my_profile, name='my_profile'),
    url(r'^interests$', views.my_likes, name='my_likes'),
    url(r'^contacts$', views.my_contacts, name='my_contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
