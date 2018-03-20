from django.conf.urls import include, url
from django.contrib import admin

from test01 import views

urlpatterns = [
    url(r'^test$', views.test),
    url(r'^index$', views.index),
    url(r'^show_date$', views.show_date),
]
