#coding=utf-8
from django.conf.urls import url
import views
urlpatterns= {
    url(r'^dept_add/$', views.depShow),
    url(r'^DepAdd/$', views.depAdd),
    url(r'^baobiao/$', views.baoBiao),
}