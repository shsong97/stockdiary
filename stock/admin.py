# -.- coding: utf-8 -.-
from django.contrib import admin
from stock.models import *
# Register your models here.
class StockAdmin(admin.ModelAdmin):
	list_display = ("stock_code", "stock_name","stock_gubun",)
	list_filter = ('stock_gubun',)
	search_fields = ['^stock_name','^stock_code']

class AlarmStockAdmin(admin.ModelAdmin):
	list_display = ('alarm_user','stock_code','price','qty','goal_price')
	list_filter = ('alarm_user',)

class FavoriteAdmin(admin.ModelAdmin):
	list_filter = ('stock_user',)
	list_display = ('stock_user','stock_code')

class UserProfileAdmin(admin.ModelAdmin):
	list_filter = ('user',)
	list_display = ('user', 'tweet_id')

class StockInformAdmin(admin.ModelAdmin):
	list_display = ("stock_code", "year", "per","pbr", "cns_eps", "cns_per", )
	list_filter = ('year', 'stock_code',)
	search_fields = ['^year']

admin.site.register(Stock, StockAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(AlarmStock, AlarmStockAdmin)
admin.site.register(StockInform, StockInformAdmin)