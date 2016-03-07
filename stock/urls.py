from django.conf.urls import include, url
from stock import views, login

urlpatterns = [
    url(r'^list$', views.list, name='list'),
    url(r'^id/(\w+)$', views.stock_id, name='stock_id'),
    url(r'^add$', views.stock_add, name='stock_add'),
    url(r'^extract/(\w+)$', views.stock_extract, name='stock_extract'),
    url(r'^deleteall$', views.stock_delete_all, name='stock_delete_all'),
    url(r'^search$', views.stock_search, name='stock_search'),
    url(r'^search_stock$', views.search_stock, name='search_stock'),
    url(r'^today$', views.today_stock, name='today_stock'),

    url(r'^alarm$', views.alarm, name='alarm'),
    url(r'^alarm/delete/(\w+)$', views.alarm_delete, name='alarm_delete'),
    url(r'^alarm/update/(\w+)$', views.alarm_update, name='alarm_update'),
    url(r'^collect_alarm$', views.collect_alarm, name='collect_alarm'),

    url(r'^favorite$', views.favorite, name='favorite'),
    url(r'^favorite/add$', views.favorite_add, name='favorite_add'),
    url(r'^favorite/list$', views.favorite_list, name='favorite_list'),
    url(r'^favorite/delete/(\w+)$', views.favorite_delete, name='favorite_delete'),
    
    url(r'^gather$', views.gathering, name='gathering'),
    url(r'^collect$', views.collect, name='collect'),
    url(r'^collect/(\d+)$', views.collect_id, name='collect_id'),
    # session
    url(r'^login/$', login.login_page, name='login'),
    url(r'^logout/$',login.logout_page, name='logout'),
    url(r'^register/$',login.register_page,name='register'), 
    url(r'^register/success/$',login.register_success),   

    url(r'^tweet_send$', views.tweet_send, name='tweet_send'),
]
