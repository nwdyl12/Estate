#coding=utf-8
from django.conf.urls import url

from frame import views

urlpatterns = [
    url(r'^frame/$',views.showFrame),
    url(r'^frame/top/$', views.top),
    url(r'^frame/left/$', views.left),
    url(r'^frame/center/$', views.center),
    url(r'^frame/down/$', views.down),
]
