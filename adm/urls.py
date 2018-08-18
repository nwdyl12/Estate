#coding=utf-8
from django.conf.urls import url

from adm import views

urlpatterns = [
    url(r'^emp_add/$',views.empAdd),
    url(r'^EmpAdd/$',views.empAddInfo),
]
