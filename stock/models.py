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


class AlarmStock(models.Model):
	alarm_user = models.ForeignKey(User,related_name='alarm_user')
	stock_code = models.ForeignKey(Stock)
	price = models.IntegerField()
	qty = models.IntegerField()
	goal_price = models.IntegerField()

	def __str__(self):
		return self.alarm_user.username


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

	def __str__(self):
		return self.stock_code.stock_code
