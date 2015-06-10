# -.- coding: utf-8 -.-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from bs4 import BeautifulSoup
import urllib
from stock.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
	return HttpResponseRedirect('/stock/list')
	
def list(request):
	objs = Stock.objects.all()
	variable = RequestContext(request,{
		'stocks':objs,
		})
	return render_to_response('stock/stock_list.html', variable)

def stock_id(request, id):
	objs = Stock.objects.all()
	url = 'http://finance.naver.com/item/main.nhn?code='+id
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)
	
	stock_id=id
	blind = soup.find('dl',{'class':'blind'})
	
	stock_dd= blind.find_all('dd')
	stock_name=stock_dd[1].text[4:]
	stock_price=stock_dd[3].text.split()[1]
	stock_price=stock_price.replace(',','')
	stock_content=blind
	stock_image = soup.find_all('img',{'id':'img_cahrt_area'})
	stock_gubun = stock_dd[2].text[-3:]


	variable = RequestContext(request,{
		'stocks':objs,
		'stock_id':stock_id,
		'stock_name':stock_name,
		'stock_price':stock_price,
		'stock_content':stock_content.text,
		'stock_image' : stock_image[0]['src'],
		'stock_gubun' : stock_gubun,
		})
	return render_to_response('stock/stock_id.html', variable)

def stock_add(request):
	stock_code = request.POST['stock_code']
	stock_name = request.POST['stock_name']
	stock_gubun = request.POST['stock_gubun']
	stock, created = Stock.objects.get_or_create(stock_code=stock_code)
	stock.stock_name=stock_name
	stock.stock_gubun=stock_gubun
	stock.save()
	return HttpResponseRedirect('/stock/list')

def stock_extract(request, classid):
	url='http://paxnet.moneta.co.kr/stock/searchStock/searchStock.jsp?section='+classid
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)
	
	stock_links = soup.find_all('a')
	
	for stock_link in stock_links:
		# print stock_link['href']
		try:
			if stock_link['href'].__contains__('http://paxnet.asiae.co.kr/asiae/stockIntro/indCurrent.jsp?code='):
				stock_code=stock_link['href'][-6:]
				stock_name=stock_link.text
				stock, created = Stock.objects.get_or_create(stock_code=stock_code)
				stock.stock_name=stock_name
				if classid=='0':
					stock.stock_gubun = "코스피"
				else:
					stock.stock_gubun = "코스닥"
				
				stock.save()
		except KeyError:
			pass

	return HttpResponseRedirect('/stock/list')

def stock_delete_all(request):
	Stock.objects.all().delete()
	return HttpResponseRedirect('/stock/list')

def stock_search(request):
	search_word=request.POST['search_key']
	if search_word:
		if len(search_word)>6:
			stock_code = search_word[:6]
			url = '/stock/id/' + stock_code
			return HttpResponseRedirect(url)

	return HttpResponseRedirect('/stock/list')

def tweet_test(request):
	objs = Stock.objects.all()
	variable = RequestContext(request,{
		'stocks':objs,
		})
	return render_to_response('stock/tweet.html', variable)

def tweet_test_send(request):
	objs = Stock.objects.all()
	variable = RequestContext(request,{
		'stocks':objs,
		})
	tweet_id = request.POST['tweet_id']
	tweet_text = request.POST['tweet_text']
	import tweet
	try:
		tweet.api.send_direct_message(screen_name=tweet_id,text=tweet_text)
	except:
		pass

	return render_to_response('stock/tweet.html',variable)

def alarm(request):
	return HttpResponse('hello')


@login_required
def favorite(request):
	favorites = Favorite.objects.filter(stock_user=request.user)


	objs = Stock.objects.all()
	variable = RequestContext(request,{
		'stocks' : objs,
		'favorites' : favorites,
		})
		
	return render_to_response('stock/favorites.html',variable)


@login_required
def favorite_add(request):
	objs = Stock.objects.all()
	variable = RequestContext(request,{
		'stocks' : objs,
		})

	if request.POST:
		user_id = request.POST['user_id']
		stock_code = request.POST['stock_code']

		user_error = stock_error = False
		user = User.objects.filter(username=user_id)
		if user is None:
			user_error = True

		stock = Stock.objects.filter(stock_code=stock_code)
		if stock is None:
			stock_error = True


		if user_error or stock_error:
			return render_to_response('stock/favorite_add.html',variable)

		else:
			favorite, created = Favorite.objects.get_or_create(stock_user=user[0], stock_code=stock[0])
			return HttpResponseRedirect('/stock/favorite')
	else:
		return render_to_response('stock/favorite_add.html',variable)

@login_required
def favorite_delete(request, user_id, stock_code):
	user =  User.objects.filter(username=user_id)
	stock = Stock.objects.filter(stock_code=stock_code)
	favorite = Favorite.objects.filter(stock_user=user, stock_code=stock)
	favorite.delete()
		
	return HttpResponseRedirect('/stock/favorite')