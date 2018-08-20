#coding=utf-8
from django.conf.urls import url
from customer import views
urlpatterns= [
    url(r'customer_care_list', views.cusCareList),
    url(r'customer_care_add', views.cusCareAdd),
    url(r'customer_care_edit', views.cusCareEdit),
    url(r'customer_care_delete', views.cusCareDelete),
    url(r'customer_care_query', views.cusCareQuery),


]
