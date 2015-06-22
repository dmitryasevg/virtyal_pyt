__author__ = 'dmitry'
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^1/',views.basicone),
    url(r'^2/',views.template_two),
]
