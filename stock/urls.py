from django.conf.urls import include, url,patterns
from stock import views

urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^id/(\w+)$', views.stock_id, name='stock_id'),
    url(r'^add$', views.stock_add, name='stock_add'),
    url(r'^extract/(\w+)$', views.stock_extract, name='stock_extract'),
    url(r'^deleteall$', views.stock_delete_all, name='stock_delete_all'),
    url(r'^search$', views.stock_search, name='stock_search'),
    url(r'^search_stock$', views.search_stock, name='search_stock'),

    url(r'^tweet_test$', views.tweet_test, name='tweet_test'),
    url(r'^tweet_test_send$', views.tweet_test_send, name='tweet_test_send'),

    url(r'^alarm$', views.tweet_test, name='alarm'),
    url(r'^favorite$', views.favorite, name='favorite'),
    url(r'^favorite/add$', views.favorite_add, name='favorite_add'),
    url(r'^favorite/delete/(\w+)/(\w+)$', views.favorite_delete, name='favorite_delete'),

]
