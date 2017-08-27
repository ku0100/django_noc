from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<device_type>[A-Za-z]+)/$', views.deviceList, name='deviceList'),
]