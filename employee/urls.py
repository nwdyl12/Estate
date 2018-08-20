#coding=utf-8
from django.conf.urls import url
from employee import views
urlpatterns=[
    url(r'^house_list/(\d*)',views.houseList),
    url(r'house_add/',views.houseAdd),
    url(r'house_edit/(\d*)',views.houseEdit),
    url(r'house_delete/(\d+)',views.houseDelete),
    url(r'house_query/',views.houseQuery)
]