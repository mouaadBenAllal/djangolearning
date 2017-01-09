"""djangoapp URL Configuration

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
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from djangoapp.settings import MEDIA_URL, MEDIA_ROOT
from djangoapp.views import AutoListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^autolist/$', AutoListView.as_view(), name='autolistview'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
