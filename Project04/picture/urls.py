from django.conf.urls import include, url
from django.contrib import admin

from picture import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^provinces$', views.provinces),
    url(r'^provinces/(\d+)$', views.provinces),
    url(r'^do_upload$', views.upload),
    url(r'^show_pic$', views.show_pic),
    url(r'^show_pic/(\d+)$', views.show_pic),
]
