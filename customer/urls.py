#coding=utf-8
from django.conf.urls import url
from customer import views

urlpatterns = [
    url(r'^customer_list1/$',views.cusList),
    url(r'^customer_add/$', views.cusAdd),
    url(r'^customer_detail/(\d+)/$', views.cusDet),
    url(r'^customer_delete/(\d+)/$', views.cusDel),
    url(r'^customer_edit/(\d+)/$', views.cusEdit),
    url(r'^customer_secadd/(\d+)/$', views.cusSecAdd),
    url(r'^customer_search/$', views.cusSea),
    url(r'^customer_type_list/$', views.cusList),
    url(r'^cusTypeQury/$', views.customQury),
    url(r'^cusTypeDel/$', views.customDel),
    url(r'^customer_type_add/$', views.cusAdd),
    url(r'^cusTypeadd/$', views.customAdd),

]





