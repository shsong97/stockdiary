from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

# from stock import views
urlpatterns = [
	url(r'^$', 'stock.views.home', name='home'),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^markdown/', include('django_markdown.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^stock/', include('stock.urls')),   
]

 