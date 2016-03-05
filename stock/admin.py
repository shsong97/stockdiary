# -.- coding: utf-8 -.-
from django.contrib import admin
from stock.models import *
from django import forms
# Register your models here.
class StockAdmin(admin.ModelAdmin):
	list_display = ('stock_code', 'stock_name','stock_gubun',)
	list_filter = ('stock_gubun',)
	search_fields = ['^stock_name','^stock_code']

class AlarmStockAdmin(admin.ModelAdmin):
	list_display = ('alarm_user','stock_code','stock_name','price','qty','goal_price')
	list_filter = ('alarm_user',)

class FavoriteAdmin(admin.ModelAdmin):
	list_filter = ('stock_user',)
	list_display = ('stock_user','stock_code','stock_name')

class UserProfileAdmin(admin.ModelAdmin):
	list_filter = ('user',)
	list_display = ('user', 'tweet_id')

class StockInformAdmin(admin.ModelAdmin):
	list_display = ('year', 'stock_code', 'stock_name', 'per','pbr', 'cns_eps', 'cns_per', 'invest_point', 'invest_remark', )
	list_filter = ('year',)
	search_fields = ['^year', '^stock_code__stock_code', ]
	ordering = ['year', 'stock_code', 'per','pbr', 'cns_eps', 'cns_per', 'invest_point', 'invest_remark',]

# Gathering model's stock_code field - verbose name
class GatheringModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		return "%s %s" % (obj.stock_code, obj.stock_name)


class GatheringAdminForm(forms.ModelForm):
	stock_code=GatheringModelChoiceField(queryset = Stock.objects.all())
	class Meta:
		model = Gathering
		fields = ['stock_code', 'gather_flag',]

		
class GatheringAdmin(admin.ModelAdmin):
	form = GatheringAdminForm
	list_display = ('stock_code', 'stock_name','gather_flag',)
	list_filter = ('gather_flag', 'stock_code', )
	search_fields = ['gather_flag','stock_code__stock_code', 'stock_name', ]
	ordering = ['stock_code']
	
admin.site.register(Stock, StockAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(AlarmStock, AlarmStockAdmin)
admin.site.register(StockInform, StockInformAdmin)
admin.site.register(StockFilter)
admin.site.register(Gathering, GatheringAdmin)