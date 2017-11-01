from django.shortcuts import render
from myadmin.models import Orders,Detail,Goods
from django.core.paginator import Paginator
from django.http import JsonResponse

#=========================订单管理=======================
#订单浏览
def ordersshow(request,pIndex):
	orderlist = Orders.objects.filter().order_by('-addtime')
	#如果有sid传过来,即分类
	sid = request.GET.get('sid',None)
	if sid:
		orderlist = orderlist.filter(status=sid)
	#分页
	p = Paginator(orderlist, 4)
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
	for i in list2:
		if i.status == 0:
			i.status = "新订单"
		if i.status == 1:
			i.status = "已发货"
		if i.status == 2:
			i.status = "已收货"
		if i.status == 3:
			i.status = "无效订单" 
	content = {"orderlist":list2,"plist":plist,'pIndex':pIndex,'previous':previous,'next':next,'sid':sid}
	return render(request,'myadmin/orders/ordersshow.html',content)

#订单详情
def ordersdetail(request,orderid):
	detail1 = Detail.objects.filter(orderid=orderid)
	content = {'detail':detail1}
	return render(request,'myadmin/orders/ordersdetail.html',content)

#订单状态修改
def ordersupdate(request):
	typeid = request.GET["orderid"]
	status = request.GET["option"]
	order = Orders.objects.get(id=typeid)
	order.status = status
	try:
		order.save()
		if status == '3':
			goodslist = Detail.objects.filter(orderid=typeid)
			for goods in goodslist:
				shop = Goods.objects.get(id=goods.goodsid)
				shop.store += goods.num
				shop.num -= goods.num
				shop.save()
		flag = True
	except:
		flag = False
	return JsonResponse({'data':flag})
#=========================end订单管理=======================