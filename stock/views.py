# -.- coding: utf-8 -.-
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required

from bs4 import BeautifulSoup
import urllib
from stock.models import *
from datetime import datetime

STOCK_URL = 'http://finance.naver.com/item/main.nhn?code='
PAX_URL = 'http://paxnet.moneta.co.kr/stock/searchStock/searchStock.jsp?section='
PAX_URL2 = 'http://paxnet.asiae.co.kr/asiae/stockIntro/indCurrent.jsp?code='

def home(request):
	return HttpResponseRedirect('/stock/list')
	
def list(request):
	objs = Stock.objects.order_by('stock_code')
	return render(request,'stock/stock_list.html',{'stocks':objs,})
	
def stock_id(request, stock_id_code):
	url = STOCK_URL+stock_id_code
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)
	
	blind = soup.find('dl',{'class':'blind'})
	
	stock_dd= blind.find_all('dd')
	stock_name=stock_dd[1].text[4:]
	stock_price=stock_dd[3].text.split()[1]
	stock_price=stock_price.replace(',','')
	stock_content=blind
	stock_image = soup.find_all('img',{'id':'img_cahrt_area'})
	stock_gubun = stock_dd[2].text[-3:]

	stock_informs = soup.find_all('em')

	pbr = per = cns_per = cns_eps = ''
	for info in stock_informs:
		try:
			if info['id']=='_pbr':
				pbr=info.text
			if info['id']=='_per':
				per=info.text
			if info['id']=='_cns_per':
				cns_per=info.text
			if info['id']=='_cns_eps':
				cns_eps=info.text

		except KeyError:
			pass

	per = per.replace(',','')
	pbr = pbr.replace(',','')
	cns_eps = cns_eps.replace(',','')
	cns_per = cns_per.replace(',','')

	if per=='':
		per=0.0
	if pbr=='':
		pbr=0.0
	if cns_eps=='':
		cns_eps=0.0
	if cns_per=='':
		cns_per=0.0
 
	variable = {
		'stock_id':stock_id_code,
		'stock_name':stock_name,
		'stock_price':stock_price,
		'stock_content':stock_content.text,
		'stock_image' : stock_image[0]['src'],
		'stock_gubun' : stock_gubun,
		'pbr' : pbr,
		'per' : per,
		'cns_per' : cns_per,
		'cns_eps' : cns_eps,
		}
	return render(request,'stock/stock_id.html', variable)

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
	url=PAX_URL+classid
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)
	
	stock_links = soup.find_all('a')
	
	for stock_link in stock_links:
		try:
			if stock_link['href'].__contains__(PAX_URL2):
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

@login_required
def stock_delete_all(request):
	if request.user.is_staff:
		Stock.objects.all().delete()
	return HttpResponseRedirect('/stock/list')

def stock_search(request):
	search_word=request.POST['search_key']
	if search_word:
		if len(search_word)>6:
			stock_code = search_word[:6]
			return HttpResponseRedirect('/stock/id/'+stock_code)
		else:
			stock_list = Stock.objects.filter(stock_name__startswith=search_word)
			return render(request, 'stock/search_list.html',{'stock_list':stock_list})
		

	return HttpResponseRedirect('/stock/list')

def search_stock(request):
	objs = Stock.objects.all()
	stock_items = []
	_pbr_from = 1
	_pbr_to = 3
	_per_from = 10
	_per_to = 30
	_cns_per_from = 10
	_cns_per_to = 30	
	_invest_point_to = 4.0

	if request.POST:
		if request.POST['pbr_from']=='':
			_pbr_from=0
		else:
			_pbr_from = request.POST['pbr_from']

		if request.POST['pbr_to']=='':
			_pbr_to=9999
		else:
			_pbr_to = request.POST['pbr_to']
			
		if request.POST['per_from']=='':
			_per_from=0
		else:		
			_per_from = request.POST['per_from']

		if request.POST['per_to']=='':
			_per_to=9999
		else:		
			_per_to = request.POST['per_to']

		if request.POST['cns_per_from']=='':
			_cns_per_from=0
		else:		
			_cns_per_from = request.POST['cns_per_from']

		if request.POST['cns_per_to']=='':
			_cns_per_to=9999
		else:		
			_cns_per_to = request.POST['cns_per_to']

		if request.POST['invest_point_to']=='':
			_invest_point_to=0.0
		else:		
			_invest_point_to = request.POST['invest_point_to']

		stock_items = StockInform.objects.filter(pbr__gt=_pbr_from,
					year = datetime.today().year,
					pbr__lt=_pbr_to,
					per__gt=_per_from,
					per__lt=_per_to,
					cns_per__gt=_cns_per_from,
					cns_per__lt=_cns_per_to,
					invest_point__gt=_invest_point_to,
					)

	return render(request,'stock/search_stock.html', {
		'stocks':objs,
		'stock_items':stock_items,
		'pbr_from' : _pbr_from,
		'pbr_to' : _pbr_to,
		'per_from' : _per_from,
		'per_to' : _per_to,
		'cns_per_from' : _cns_per_from,
		'cns_per_to' : _cns_per_to,	
		'invest_point_to' : _invest_point_to,
		})


def tweet_send(request):
	if request.POST:
		tweet_id = request.POST['tweet_id']
		tweet_text = request.POST['tweet_text']
		import tweet
		try:
			tweet.api.send_direct_message(screen_name=tweet_id,text=tweet_text)
		except:
			pass
	return render(request,'stock/tweet.html')


def alarm(request):
	objs = Stock.objects.all()
	alarm_list = AlarmStock.objects.filter(alarm_user=request.user)
	if request.POST:
		stock_code=None
		search_word=request.POST['stock_name']
		if search_word:
			if len(search_word)>6:
				stock_code = search_word[:6]
		
		if stock_code:
			stock = Stock.objects.filter(stock_code = stock_code)
			
			qty = request.POST['qty']
			if qty=='':
				qty=1

			goal_price = request.POST['goal_price']
			if goal_price=='':
				goal_price=0

			if stock:
				alarm_stock, created  = AlarmStock.objects.get_or_create(
					alarm_user = request.user, 
					stock_code = stock[0],
					price = 0,
					qty = qty,
					goal_price = goal_price,
					)
	return render(request,'stock/stock_alarm.html',{'alarm_list':alarm_list,'stocks':objs,})

@login_required()
def alarm_delete(request, stock_code):
	stock = Stock.objects.filter(stock_code=stock_code)
	alarm_stock = AlarmStock.objects.filter(alarm_user=request.user, stock_code=stock)
	alarm_stock.delete()
		
	return HttpResponseRedirect('/stock/alarm')

@login_required()
def alarm_update(request, stock_code):
	stock = Stock.objects.filter(stock_code=stock_code)
	alarm_stock = AlarmStock.objects.filter(alarm_user=request.user, stock_code=stock)
	if alarm_stock:
		alarm1 = alarm_stock[0]
		qty = 0 
		goal = 0
		if request.GET.get('qty_code'):
			qty = request.GET['qty_code']
		if request.GET.get('goal_code'):
			goal = request.GET['goal_code']
			goal = goal.replace(',','')
		
		alarm1.qty = qty
		alarm1.goal_price = goal
		alarm1.save()
		
	return HttpResponseRedirect('/stock/alarm')

@login_required()
def alarm_get_list(request):
	alarm_list = AlarmStock.objects.filter(alarm_user=request.user)
	message = "아래종목이 목표가에 도달했습니다\n"
	target_list = ""
	for ob in alarm_list:
		if ob.price > ob.goal_price:
			st_code = str(ob.stock_code)
			st_name = str(ob.stock_name.encode('utf-8'))
			st_goal_price = str(ob.goal_price)
			target_list += st_name + "(" + st_code + ")=>" + st_goal_price + "\n"
	
	if target_list=="":
		message = "목표달성한 종목이 없습니다."
	else:
		message += target_list
	print message
	return JsonResponse({'message':message})

@login_required()
def collect_alarm(request):
	objs = AlarmStock.objects.filter(alarm_user=request.user)
	for obj in objs:
		stock_id_code = obj.stock_code.stock_code

		url = STOCK_URL+stock_id_code
		html = urllib.urlopen(url)
		soup = BeautifulSoup(html)
		
		blind = soup.find('dl',{'class':'blind'})
		
		stock_dd= blind.find_all('dd')
		stock_price=stock_dd[3].text.split()[1]
		stock_price=stock_price.replace(',','')
		
		obj.price = stock_price
		obj.save()

	return HttpResponseRedirect('/stock/alarm')

@login_required()
def favorite(request):
	favorites = Favorite.objects.filter(stock_user=request.user)
	objs = Stock.objects.all()
	return render(request,'stock/favorites.html',{
		'stocks' : objs,
		'favorites' : favorites,
		})

@login_required()
def favorite_list(request):
	favorites = Favorite.objects.filter(stock_user=request.user)
	return render(request,'stock/favorite_list.html',{
		'favorites' : favorites,
		})
	
@login_required()
def favorite_add(request):
	objs = Stock.objects.all()
	if request.POST:
		search_word=request.POST['stock_code']
		if search_word:
			if len(search_word)>6:
				stock_code = search_word[:6]
			
		user_error = stock_error = False
		user = request.user
		if user:			
			user_error = False
		else:
			user_error = True

		stock = Stock.objects.filter(stock_code=stock_code)
		if stock is None:
			stock_error = True

		if user_error or stock_error:
			return render(request,'stock/favorite_add.html')

		else:
			favorite, created = Favorite.objects.get_or_create(stock_user=user, stock_code=stock[0])
			return HttpResponseRedirect('/stock/favorite')
	else:
		return render(request,'stock/favorite_add.html',{'stocks' : objs})


@login_required()
def favorite_delete(request, stock_code):
	stock = Stock.objects.filter(stock_code=stock_code)
	favorite = Favorite.objects.filter(stock_user=request.user, stock_code=stock)
	favorite.delete()
		
	return HttpResponseRedirect('/stock/favorite')


def today_stock(request):
	stock_items = []
	
	stock = StockFilter.objects.filter(filter_name='todaystock')

	_per_from = stock[0].per_from
	_per_to = stock[0].per_to
	_pbr_from = stock[0].pbr_from
	_pbr_to = stock[0].pbr_to

	_cns_per_from = stock[0].cns_per_from
	_cns_per_to = stock[0].cns_per_to
	_cns_eps_from = stock[0].cns_eps_from
	_cns_eps_to = stock[0].cns_eps_to
	_invest_point_to = stock[0].invest_point_to
	current_year= datetime.today().year
	# print _pbr_from
	stock_items = StockInform.objects.filter(
		year=current_year,

		per__gt=_per_from, 
		per__lt=_per_to,
		pbr__gt=_pbr_from, 
		pbr__lt=_pbr_to, 

		cns_per__gt=_cns_per_from, 
		cns_per__lt=_cns_per_to,
		cns_eps__gt=_cns_eps_from, 
		cns_eps__lt=_cns_eps_to,
		invest_point__gt=_invest_point_to,
		).order_by('per')

	return render(request,'stock/today.html',{
		'stock_items':stock_items,
		})

def stock_info_collect(stock_id_code):
	url = STOCK_URL+stock_id_code
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html)

	stock_informs = soup.find_all('em')
	pbr = per = cns_per = cns_eps = ''
	for info in stock_informs:
		try:
			if info['id']=='_pbr':
				pbr=info.text
			if info['id']=='_per':
				per=info.text
			if info['id']=='_cns_per':
				cns_per=info.text
			if info['id']=='_cns_eps':
				cns_eps=info.text

		except KeyError:
			pass

	per = per.replace(',','')
	pbr = pbr.replace(',','')
	cns_eps = cns_eps.replace(',','')
	cns_per = cns_per.replace(',','')

	invest_point = 0
	invest_remark = ''
	
	invest_info = soup.find_all('table',attrs={'class':'rwidth'})
	for invest_item in invest_info:
		span_info = invest_item.find('span',attrs={'class':'f_up'})
		if span_info:
			invest_point = float(str(span_info.find('em').text))
			invest_remark = span_info.text
		# print span_info

	if per=='':
		per=0.0
	if pbr=='':
		pbr=0.0
	if cns_eps=='':
		cns_eps=0.0
	if cns_per=='':
		cns_per=0.0

	try:
		year = datetime.today().year
		stock = Stock.objects.filter(stock_code=stock_id_code)[0]
		if stock:
			stock_infos = StockInform.objects.filter(stock_code=stock, year=year)
			if stock_infos:
				stock_info = stock_infos[0]
				stock_info.per = per
				stock_info.pbr = pbr
				stock_info.cns_per = cns_per
				stock_info.cns_eps = cns_eps
				stock_info.invest_point = invest_point
				stock_info.invest_remark = invest_remark
				stock_info.save()
			else:
				stock_info, created = StockInform.objects.get_or_create(stock_code=stock, 
					year= year,
					per = per,
					pbr = pbr,
					cns_per = cns_per,
					cns_eps = cns_eps,
					invest_point = invest_point,
					invest_remark = invest_remark,
					)
	except KeyError:
		pass
	
def gathering(request):
	objs = Gathering.objects.filter(gather_flag='Y')
	for obj in objs:
		stock_info_collect(obj.stock_code.stock_code)

	return render(request,'stock/gathering.html', {
		'stocks':objs,
		})	

def collect_id(request, stockid):
	objs = Stock.objects.filter(stock_code__istartswith=stockid).order_by('stock_code')
	for obj in objs:
		stock_info_collect(obj.stock_code)
	
	return render(request,'stock/collect.html', {
		'stocks':objs,
		})

def collect(request):
	variable = {}
	objs=[]
	if request.GET:
		if request.GET.get('start_key'):
			start_key = request.GET['start_key']

			objs = Stock.objects.filter(stock_code__istartswith=start_key).order_by('stock_code')
			from_time = datetime.today()
			for obj in objs:
				print obj.stock_code
				stock_id = obj.stock_code
				stock_info_collect(stock_id)
			to_time = datetime.today()
			print "End time : "
			print to_time-from_time
			
	return render(request,'stock/collect.html', {
				'stocks':objs,
				})
