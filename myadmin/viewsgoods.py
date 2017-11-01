from django.shortcuts import render
from myadmin.models import Type,Goods
from django.core.paginator import Paginator
import time,os
from PIL import Image

#================商品类别=========================
#商品类别浏览
def typeshow(request):
	typelist = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for list1 in typelist:
		if list1.pid !=0 :
			typeG = Type.objects.get(id=list1.pid)
			list1.pid = typeG.name
			row = list1.path.count(',')
			list1.row = "----"*(row-1)+"|"
	content = {'typelist':typelist}
	return render(request,'myadmin/type/typeshow.html',content)

#商品类别添加
def typeadd(request):
	typelist = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for list1 in typelist:
		if list1.pid !=0 :
			row = list1.path.count(',')
			list1.row = row
			list1.line = "----"*(row-1)+"|"
	content = {'typelist':typelist}
	return render(request,'myadmin/type/typeadd.html',content)
#执行添加
def typeinsert(request):
	fid = request.POST['fid']
	cid = request.POST['cid']
	type1 = Type()
	if fid == '0':
		path="0,"
	else:
		type2 = Type.objects.get(id=fid)
		path = type2.path + fid + ','
	type1.name = cid
	type1.pid = fid
	type1.path = path
	try:
		type1.save()
		info = "添加成功"
	except:
		info = "添加失败"
	content = {"info":info}
	return render(request,'myadmin/info.html',content) 

#商品类别修改
def typeedit(request,typeid):
	type1 = Type.objects.get(id=typeid)
	if type1.pid == 0:
		type1.pid = '无'
	else:
		typeG = Type.objects.get(id=type1.pid)
		type1.pid = typeG.name
	content = {'typelist':type1}
	return render(request,'myadmin/type/typeedit.html',content)
#执行修改
def typeupdate(request):
	tid = request.POST['tid']
	tname = request.POST['tname']
	type1 = Type.objects.get(id=tid)
	type1.name = tname
	try:
		type1.save()
		info = "修改成功"
	except:
		info = "修改失败"
	content = {"info":info}
	return render(request,'myadmin/info.html',content) 

#商品类别删除
def typedel(request,typeid):
	try:
		type1 = Type.objects.get(id=typeid)
		type2 = Type.objects.filter(pid=typeid)
		if not type2.exists():
			type1.delete()
			info = "删除成功"
		else:
			info = "删除失败!含有子类别"
	except:
		info = "删除失败"
	content = {"info":info}
	return render(request,'myadmin/info.html',content) 
#================end商品类别=========================

#================商品操作=========================
#商品浏览
def goodsshow(request,pIndex):
	goodslist = Goods.objects.filter()
	p = Paginator(goodslist, 6)
	if pIndex == '':
	    pIndex = '1'
	pIndex = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range
	if list2.has_previous():
		previous = list2.previous_page_number()
	else:
		previous = False
	if list2.has_next():
		next = list2.next_page_number()
	else:
		next = False
	for i in  list2:
		if i.typeid != 0:
			type1 = Type.objects.get(id = i.typeid)
			i.typeid = type1.name
		if i.state == 1:
			i.state = "新添加"
		elif i.state == 2:
			i.state = "在售"
		else:
			i.state = "下架"
	content = {'goodslist':list2,'plist':plist,'pIndex':pIndex,'previous':previous,'next':next}
	return render(request,'myadmin/goods/goodsshow.html',content)

#商品添加
def goodsadd(request):
	typelist = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for list1 in typelist:
		if list1.pid != 0:
			row = list1.path.count(',')
			list1.row = "----"*(row-1)+"|"
	content = {'typelist':typelist}
	return render(request,'myadmin/goods/goodsadd.html',content)
#执行添加
def goodsinsert(request):
	try:
		commodity = Goods()
		commodity.typeid = request.POST['typeid']
		commodity.goods = request.POST['name']
		commodity.company = request.POST['company']
		commodity.descr = request.POST['descr']
		commodity.price = request.POST['price']
		imgfile = request.FILES.get("imgfile",None)
		#图片使用时间戳命名并存入到指定文件
		imgname = str('{:.4f}'.format(time.time())) + '.' + imgfile.name.split('.').pop()
		destination = open(os.path.join("./static/imgs/goods/",imgname),'wb+')
		for chunk in imgfile.chunks():  
			destination.write(chunk)  
		destination.close()
		commodity.picname = imgname
		#生成不同的缩放图片
		im = Image.open("./static/imgs/goods/"+imgname)
		#2601*261
		im.thumbnail((261,261))
		im.save("./static/imgs/goods/"+'m'+imgname)
		#100*100
		im.thumbnail((100,100))
		im.save("./static/imgs/goods/"+'l'+imgname)
		commodity.state = request.POST['state']
		commodity.store = request.POST['number']
		commodity.addtime = time.strftime('%Y%m%d%H%M',time.localtime())
		commodity.save()
		info = "添加成功"
	except:
		info = "添加失败"
		if imgfile:
			os.remove(os.path.join("./static/imgs/goods/",imgname))
			os.remove(os.path.join("./static/imgs/goods/",'m'+imgname))
			os.remove(os.path.join("./static/imgs/goods/",'l'+imgname))
	content = {"info":info}
	return render(request,'myadmin/info.html',content) 
#商品修改
def goodsedit(request,goodsid):
	typelist = Type.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
	for list1 in typelist:
		if list1.pid != 0:
			row = list1.path.count(',')
			list1.row = "----"*(row-1)+"|"
	goods = Goods.objects.get(id=goodsid)
	content = {'goods':goods,'typelist':typelist}
	return render(request,'myadmin/goods/goodsedit.html',content)
#执行修改
def goodsupdate(request):
	try:
		commodity = Goods.objects.get(id=request.POST['goodsid'])
		commodity.typeid = request.POST['typeid']
		commodity.goods = request.POST['name']
		commodity.company = request.POST['company']
		commodity.descr = request.POST['descr']
		commodity.price = request.POST['price']
		imgfile = request.FILES.get("imgfile",None)
		if imgfile:
			os.remove(os.path.join("./static/imgs/goods/",commodity.picname))
			os.remove(os.path.join("./static/imgs/goods/",'m'+commodity.picname))
			os.remove(os.path.join("./static/imgs/goods/",'l'+commodity.picname))
			imgname = str('{:.4f}'.format(time.time())) + '.' + imgfile.name.split('.').pop()
			destination = open(os.path.join("./static/imgs/goods/",imgname),'wb+')
			for chunk in imgfile.chunks():      # 分块写入文件  
				destination.write(chunk)  
			destination.close()
			commodity.picname = imgname
			#生成不同的缩放图片
			im = Image.open("./static/imgs/goods/"+imgname)
			#206*206
			im.thumbnail((206,206))
			im.save("./static/imgs/goods/"+'m'+imgname)
			#100*100
			im.thumbnail((100,100))
			im.save("./static/imgs/goods/"+'l'+imgname)
		commodity.state = request.POST['state']
		commodity.store = request.POST['number']
		commodity.save()
		info = "修改成功"
	except:
		info = "修改失败"
		if imgfile:
			os.remove(os.path.join("./static/imgs/goods/",imgname))
			os.remove(os.path.join("./static/imgs/goods/",'m'+imgname))
			os.remove(os.path.join("./static/imgs/goods/",'l'+imgname))
	content = {"info":info}
	return render(request,'myadmin/info.html',content) 

#商品删除
def goodsdel(request,goodsid):
	goods1 = Goods.objects.get(id=goodsid)
	if goods1.state != 1:
		info = "删除失败,只能删除新添加商品"
		content = {"info":info}
		return render(request,'myadmin/info.html',content)
	try:
		os.remove(os.path.join("./static/imgs/goods/",goods1.picname))
		os.remove(os.path.join("./static/imgs/goods/",'m'+goods1.picname))
		os.remove(os.path.join("./static/imgs/goods/",'l'+goods1.picname))
		goods1.delete()
		info = "删除成功"
	except:
		info = "删除失败"
	content = {"info":info}
	return render(request,'myadmin/info.html',content) 
#================end商品操作=========================