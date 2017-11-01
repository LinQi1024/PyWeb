from django.shortcuts import render
from myweb.models import Users,District,Orders,Detail,Goods
from django.http import JsonResponse
import hashlib
from django.core.paginator import Paginator

#个人信息
def userinfo(request):
 	user = Users.objects.get(id=request.session["userid"])
 	if user.sex == 1:
 		user.sex = '男'
 	else:
 		user.sex = '女'
 	content = {'user':user}
 	return render(request,"myweb/userinfo.html",content)

#个人信息修改
def usinfoch(request):
	user = Users.objects.get(id=request.session["userid"])
	content = {'user':user}
	return render(request,"myweb/usinfoch.html",content)

#执行个人信息修改
def dousinfoch(request):
	user = Users.objects.get(id=request.session["userid"])
	try:
		user.name = request.POST['name']
		user.sex = request.POST['sex']
		user.code = request.POST['code']
		user.phone = request.POST['phone']
		user.email = request.POST['email']
		user.save()
		info = "修改成功"
	except:
		info = "修改失败"
	content = {'info':info}
	return render(request,"myweb/info_user.html",content)

#密码重置
def passwdreset(request):
	return render(request,"myweb/passwdreset.html")

#执行密码重置
def dopwreset(request):
	passwd = request.POST['passwd']
	user = Users.objects.get(id=request.session["userid"])
	try:
		m = hashlib.md5()
		m.update(bytes(passwd,encoding="utf8"))
		user.passwd = m.hexdigest()
		user.save()
		info = "密码重置成功"
	except:
		info = "密码重置失败"
	content = {"info":info}
	return render(request,"myweb/info_user.html",content)

#收货地址管理
def addressmange(request):
	user = Users.objects.get(id=request.session["userid"])
	address = user.address
	district = []
	#获取一级地区范围
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
		content = {"addrlist":addrlist,"addrdetail":addrdetail,"district":district}
	else:
		content = {"district":district}
	return render(request,"myweb/addressmange.html",content)

# 加载对应的城市信息，并json格式ajax方式响应
def district(request,upid):
    dlist = District.objects.filter(upid=upid)
    list1 = []
    for ob in dlist:
        list1.append({'id':ob.id,'name':ob.name})
    return JsonResponse({'data':list1})

#保存地址
def saveaddr(request):
	addrlist = request.POST.getlist('district')
	addrdetail = request.POST['address']
	user = Users.objects.get(id=request.session["userid"])
	user.address = ' '.join(addrlist) + ' ' + addrdetail
	try:
		user.save()
		info = "地址编辑成功"
	except:
		info = "地址编辑失败"
	content = {"info":info}
	return render(request,"myweb/info_user.html",content)

#订单浏览
def orderviews(request,pIndex):
	user = Users.objects.get(id=request.session["userid"])
	orderlist = Orders.objects.filter(uid=user.id)
	sid = request.GET.get('sid',None)
	if sid:
		orderlist = orderlist.filter(status=sid)
	#分页
	p = Paginator(orderlist, 5)
	if pIndex == '':
	    pIndex = '1'
	pIndex = int(pIndex)
	list2 = p.page(pIndex)
	if list2.has_previous():
		previous = list2.previous_page_number()
	else:
		previous = False
	if list2.has_next():
		next = list2.next_page_number()
	else:
		next = False
	plist = p.page_range
	#替换状态
	for order in list2:
		if order.status == 0:
			order.status = "新订单"
		elif order.status == 1:
			order.status = "已发货"
		elif order.status == 2:
			order.status = "已收货"
		else:
			order.status = "已失效"
	content = {"orderlist":list2,"plist":plist,'pIndex':pIndex,'previous':previous,'next':next,'sid':sid}
	return render(request,"myweb/orderviews.html",content)

#查看订单详情
def orderdetail(request):
	orderid = request.GET['orderid']
	ordershop = Detail.objects.filter(orderid=orderid)
	shoplist = []
	for shop in ordershop:
		goods = shop.toDict()
		goods['picname'] = 'l' + Goods.objects.get(id=shop.goodsid).picname
		shoplist.append(goods)
	return JsonResponse({'shoplist':shoplist})

#取消订单
def ordercancel(request):
	orderid = request.GET['orderid']
	try:
		order = Orders.objects.get(id=orderid)
		order.status = 3
		order.save()
		goodslist = Detail.objects.filter(orderid=orderid)
		for goods in goodslist:
			shop = Goods.objects.get(id=goods.goodsid)
			shop.store += goods.num
			shop.num -= goods.num
			shop.save()
		info = True
	except:
		info = False
	content={'info':info}
	return JsonResponse(content)



