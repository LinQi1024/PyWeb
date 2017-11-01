from django.shortcuts import render
from myweb.models import Goods,Users,Orders,Detail,District
from django.http import JsonResponse
import time

#=========================购物车===================
#添加购物车
def cartadd(request):
	gid=request.POST['goodsid']
	gnum=int(request.POST['goodsnum'])
	if 'cart' in request.session:
		shoplist = request.session['cart']
	else:
		shoplist = {}
	if gid in shoplist:
		shoplist[gid]['gnum'] += int(gnum)
		#判断是否超出库存,如果超出,则设数量为库存数量
		hasnum = Goods.objects.get(id=gid).store
		if shoplist[gid]['gnum'] > hasnum:
			shoplist[gid]['gnum'] = hasnum
	else:
		goods = Goods.objects.get(id=gid)
		goods = goods.toDict()
		goods['gnum'] = gnum
		shoplist[gid]=goods
	request.session['cart'] = shoplist
	info = "添加成功"
	content = {'info':info,'flag':'cartadd'}
	return render(request,'myweb/info.html',content)

#浏览购物车
def cartshow(request):
	if 'cart' in request.session:
		shoplist = request.session['cart']
	else:
		shoplist = {}
	content = {'shoplist':shoplist}
	if request.is_ajax():
		return JsonResponse(content)
	else:
		return render(request,'myweb/cartshow.html',content)

#购物车删除商品
def cartgdel(request):
	goodsid = request.GET['goodsid']
	shoplist = request.session['cart']
	flag = shoplist.pop(goodsid,None)
	if flag:
		data = True
		request.session['cart'] = shoplist
	else:
		data = False
	return JsonResponse({'data':data})

#购物车清空
def cartclaer(request):
	del request.session['cart']
	return JsonResponse({})

#购物车商品数量
def cartgchan(request):
	goodsid = request.GET['goodsid']
	goodsnum = request.GET['goodsnum']
	shoplist = request.session['cart']
	shoplist[goodsid]['gnum'] = int(goodsnum)
	request.session['cart'] = shoplist
	return JsonResponse({})
#=========================end 购物车===================

#=========================订单=========================
#结算后的订单页面
def orderadd(request):
	#获取用户信息
	userid = request.session["userid"]
	user = Users.objects.get(id=userid)
	#获取收货地址信息
	address = user.address
	district = []
	fanwei = District.objects.filter(upid=0)
	district.append(fanwei)
	if address:
		addrlist = address.split(' ')
		addrdetail = addrlist.pop()
		for i in addrlist:
			#在当前地区范围中查询同级地区
			diqu = fanwei.get(name=i)
			fanwei =  District.objects.filter(upid=diqu.id)
			if fanwei.exists():
				district.append(fanwei)
		dizhi = {"addrlist":addrlist,"addrdetail":addrdetail,"district":district}
	else:
		dizhi = {"district":district}
	#获取要加入订单的商品信息
	orderglist = {} 
	totalpri = 0
	order = {}
	cartlist = request.session["cart"]
	goodslist = request.POST.getlist('chiocegoods')
	for goods in goodslist:
		orderglist[goods] = cartlist[goods]
		totalpri += cartlist[goods]['gnum'] * cartlist[goods]['price']
	order['goods'] = orderglist
	order['total'] = totalpri
	request.session["order"] = order
	content = {"user":user,'dizhi':dizhi,'orderglist':orderglist}
	return render(request,'myweb/orderaddshow.html',content)

#订单确认
def orderconfirm(request):
	getgoodsinfo = {}
	getgoodsinfo['linkman'] = request.POST["linkman"]
	getgoodsinfo['phone'] = request.POST["phone"]
	addrlist = request.POST.getlist('district')
	addrdetail = request.POST['address']
	getgoodsinfo['address'] = ' '.join(addrlist) + ' ' + addrdetail
	getgoodsinfo['code'] = request.POST['code']
	order = request.session["order"]
	order['getinfo'] = getgoodsinfo
	request.session["order"] = order
	content={'order':order}
	return render(request,'myweb/orderconfirm.html',content)

#订单已确认
def ordersure(request):
	#取出订单信息
	order = request.session["order"]
	total = order["total"]
	goods = order["goods"]
	getinfo = order["getinfo"]
	#商品库存判断
	for g in goods:
		shop1 = Goods.objects.get(id=goods[g]['goodsid'])
		if goods[g]['gnum'] > shop1.store:
			info = False
			content = {'info':info}
			return JsonResponse(content)
	#取出购物车信息,以便删除订单中的商品
	cartlist = request.session["cart"]
	try:
		#存入订单数据库
		toorder = Orders()
		toorder.uid = request.session['userid']
		toorder.linkman = getinfo['linkman']
		toorder.address = getinfo['address']
		toorder.code = getinfo['code']
		toorder.phone = getinfo['phone']
		toorder.addtime = time.strftime('%Y%m%d%H%M',time.localtime())
		toorder.total = total
		toorder.status = 0 
		toorder.save()
		#存入详情库
		for i in goods:
			todetail = Detail()
			todetail.orderid = toorder.id
			todetail.goodsid = goods[i]['goodsid']
			todetail.name = goods[i]['goods']
			todetail.price = goods[i]['price']
			todetail.num = goods[i]['gnum']
			todetail.save()
			#在购物车中删除订单中的商品
			cartlist.pop(i,None)
			#改变商品的购买量
			shop = Goods.objects.get(id = i)
			shop.num += todetail.num
			shop.store -= todetail.num
			shop.save()
		request.session["cart"] = cartlist
		del request.session['order']
		info = True
	except:
		info = False
	content = {"info":info}
	return JsonResponse(content)


#=========================end 订单=====================