# -.- coding: utf-8 -.-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stock(models.Model):
	stock_code = models.CharField(max_length=10)
	stock_name = models.CharField(max_length=100)
	stock_gubun = models.CharField(max_length=10, default="코스피")

	def __str__(self):
		return self.stock_code

class Favorite(models.Model):
	stock_user = models.ForeignKey(User,related_name='stock_user')
	stock_code = models.ForeignKey(Stock)

	def __str__(self):
		return self.stock_user.username

	@property
	def stock_name(self):
		return self.stock_code.stock_name

class AlarmStock(models.Model):
	alarm_user = models.ForeignKey(User,related_name='alarm_user')
	stock_code = models.ForeignKey(Stock)
	price = models.IntegerField()
	qty = models.IntegerField()
	goal_price = models.IntegerField()

	def __str__(self):
		return self.alarm_user.username

	@property
	def stock_name(self):
		return self.stock_code.stock_name


class UserProfile(models.Model):
	user = models.ForeignKey(User, related_name='user_profile')
	tweet_id = models.CharField(max_length=30)

	def __str__(self):
		return self.user.username

class StockInform(models.Model):
	stock_code = models.ForeignKey(Stock)
	year = models.IntegerField()
	per = models.FloatField()
	pbr = models.FloatField()
	cns_per = models.FloatField()
	cns_eps = models.FloatField()
	invest_point = models.FloatField(default=0.0)
	invest_remark = models.CharField(max_length=10,default='')

	def __str__(self):
		return self.stock_code.stock_code

	@property
	def stock_name(self):
		return self.stock_code.stock_name

	
class StockFilter(models.Model):
	filter_name = models.CharField(max_length=50)
	per_from = models.FloatField()
	per_to = models.FloatField()
	pbr_from = models.FloatField()
	pbr_to = models.FloatField()
	cns_per_from = models.FloatField()
	cns_per_to = models.FloatField()
	cns_eps_from = models.FloatField()
	cns_eps_to = models.FloatField()
	
	def __str__(self):
		return self.filter_name	

class Gathering(models.Model):
	stock_code = models.ForeignKey(Stock)
	gather_flag = models.CharField(max_length=1,default='Y')
	
	def stock_value(self):
		return self.stock_code.stock_name
		
	stock_name = property(stock_value)
	