#coding=utf-8
from django.conf.urls import url
import views
urlpatterns= {
    url(r'^customer_type_list/$', views.cusList),
    url(r'^cusTypeQury/$', views.customQury),
    url(r'^cusTypeDel/$', views.customDel),
    url(r'^customer_type_add/$', views.cusAdd),
    url(r'^cusTypeadd/$', views.customAdd),


}