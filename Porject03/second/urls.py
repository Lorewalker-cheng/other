from django.conf.urls import include, url
from django.contrib import admin

from second import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^center/$', views.center),
]
