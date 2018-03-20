from django.conf.urls import url

from fist import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^show_data/(\d+)/$', views.show_data),
    url(r'^add_data/$', views.add_data),
    url(r'^del_data/(\d+)/$', views.del_data)
]
