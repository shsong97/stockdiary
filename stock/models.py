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