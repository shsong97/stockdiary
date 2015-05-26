from django.contrib import admin
from stock.models import *
# Register your models here.
class StockAdmin(admin.ModelAdmin):
	list_display = ("stock_code", "stock_name","stock_gubun",)
	list_filter = ('stock_gubun',)
	search_fields = ['^stock_name','^stock_code']
admin.site.register(Stock,StockAdmin)
