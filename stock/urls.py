from django.conf.urls import include, url
from stock import views

urlpatterns = [
    url(r'^list/', views.list, name='list'),
    url(r'^id/(\d+)', views.stock_id, name='stock_id'),
    url(r'^add', views.stock_add, name='stock_add'),
    url(r'^extract/(\d+)', views.stock_extract, name='stock_extract'),
    url(r'^deleteall', views.stock_delete_all, name='stock_delete_all'),
    url(r'^search', views.stock_search, name='stock_search'),
] 