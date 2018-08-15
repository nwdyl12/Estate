#coding=utf-8
from django.conf.urls import url

from RealEstate import views

urlpatterns = [
    url(r'^$',views.login),
]