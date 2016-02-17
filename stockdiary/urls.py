from django.conf.urls import include, url
from django.contrib import admin
from stock import views
admin.autodiscover()

# from stock import views
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^stock/', include('stock.urls')),   
]

 