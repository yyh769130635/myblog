# Author:peter young
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^1/$', views.index),
]