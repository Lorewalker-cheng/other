from django.conf.urls import include, url
from django.contrib import admin

from picture import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^provinces/$', views.provinces),
    url(r'^provinces/(\d+)/$', views.provinces),
]
