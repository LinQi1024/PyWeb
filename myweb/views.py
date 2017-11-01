from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from myweb.models import Goods,Type,Users
import hashlib,time
#排序函数
def sort(request,goodslist,sortid):
	if sortid == '1':
		goodslist = goodslist.order_by('-clicknum')
	elif sortid == '2':
		goodslist = goodslist.order_by('-num')
	elif sortid == '3':
		goodslist = goodslist.order_by('price')
	elif sortid == '4':
		goodslist = goodslist.order_by('-price')
	return goodslist

#前端主页
def index(request):
	hotgoods = Goods.objects.order_by('-num')[0:4]
	for goods in hotgoods:
		goods.picname = 'm'+goods.picname
	rqgoods = Goods.objects.order_by('-clicknum')[0:6]
	for goods in rqgoods:
		goods.picname = 'm'+goods.picname
	content = {'hotgoods':hotgoods,'rqgoods':rqgoods}
	return render(request,'myweb/index.html',content)

#全部商品页
def goodslist(request,typeid):
	#全部在售商品
	if typeid == '0':
		goodslist = Goods.objects.filter(state=2)
		type1 = None
	#类别在售商品
	else:
		type1 = Type.objects.filter(path__contains=','+str(typeid)+',')
		#如果有子类别,则获取商品类别在子类别id中的在售商品
		if type1.exists():
			goodslist = Goods.objects.filter(state=2).filter(typeid__in=Type.objects.only('id').filter(path__contains=','+str(typeid)+','))
			type1 = Type.objects.filter(pid=typeid)
		else:
			goodslist = Goods.objects.filter(state=2).filter(typeid=typeid)
			type1 = Type.objects.get(id=typeid)
			type1 = Type.objects.get(id=type1.pid)
			type1 = Type.objects.filter(pid=type1.id)
	#如果请求排序
	sortid = request.GET.get('sort',None)
	if sortid:
		goodslist=sort(request,goodslist,sortid)
	#跟换图片名字为m类型
	for goods in goodslist:
		goods.picname = 'm'+goods.picname
	content = {"goodslist":goodslist,'type1':type1}
	return render(request,'myweb/goodslist.html',content)

#商品详情页
def information(request,goodsid):
	goods = Goods.objects.get(id=goodsid)
	goods.clicknum += 1
	goods.save()
	goods.lpicname = 'l'+goods.picname
	content = {"goods":goods}
	return render(request,'myweb/information.html',content)

#登录
def login(request):
	return render(request,'myweb/login.html')
#返回验证码
def verify(request):
	#引入随机函数模块
	import random
	from PIL import Image, ImageDraw, ImageFont
	#定义变量，用于画面的背景色、宽、高
	#bgcolor = (random.randrange(20, 100), random.randrange(
	#    20, 100),100)
	bgcolor = (242,164,247)
	width = 200
	height = 40
	#创建画面对象
	im = Image.new('RGB', (width, height), bgcolor)
	#创建画笔对象
	draw = ImageDraw.Draw(im)
	#调用画笔的point()函数绘制噪点
	for i in range(0, 100):
	    xy = (random.randrange(0, width), random.randrange(0, height))
	    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
	    draw.point(xy, fill=fill)
	#定义验证码的备选值
	str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
	#随机选取4个值作为验证码
	rand_str = ''
	for i in range(0, 4):
	    rand_str += str1[random.randrange(0, len(str1))]
	#构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
	font = ImageFont.truetype('static/public/STXIHEI.TTF',21)
	#font = ImageFont.load_default().font
	#构造字体颜色
	fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
	#绘制4个字
	draw.text((5, -5), rand_str[0], font=font, fill=fontcolor)
	draw.text((25, -5), rand_str[1], font=font, fill=fontcolor)
	draw.text((50, -5), rand_str[2], font=font, fill=fontcolor)
	draw.text((75, -5), rand_str[3], font=font, fill=fontcolor)
	#释放画笔
	del draw
	#存入session，用于做进一步验证
	request.session['verifycode'] = rand_str
	"""
	python2的为
	# 内存文件操作
	import cStringIO
	buf = cStringIO.StringIO()
	"""
	# 内存文件操作-->此方法为python3的
	import io
	buf = io.BytesIO()
	#将图片保存在内存中，文件类型为png
	im.save(buf, 'png')
	#将内存中的图片数据返回给客户端，MIME类型为图片png
	return HttpResponse(buf.getvalue(), 'image/png')
#执行登录
def dologin(request):
	vc1 = request.POST['verifycode'].lower()
	vc2 = request.session['verifycode'].lower()
	if vc1 != vc2:
		info = "验证码错误"
		content = {'info':info}
		return render(request,'myweb/login.html',content)
	try:
		user = Users.objects.get(username=request.POST['username'])
		if user.state == 2:
			info = "已禁用"
		else:
			passwd1 = request.POST['passwd']
			m = hashlib.md5()
			m.update(bytes(passwd1,encoding="utf8"))
			passwd2 = m.hexdigest()
			if passwd2 == user.passwd:
				request.session['userid'] = user.id
				return redirect(reverse('index'))
			else:
				info = "账号密码错误"
	except:
	 	info = "账号密码错误"
	content = {'info':info}
	return render(request,'myweb/login.html',content)
#注册
def register(request):
	return render(request,'myweb/register.html')
#执行注册
def doregister(request):
	user = Users.objects.filter(username=request.POST['username'])
	if user.exists():
		info = "用户已存在"
	else:
		user = Users()
		user.username = request.POST['username']
		m = hashlib.md5()
		m.update(bytes(request.POST['passwd'],encoding="utf8"))
		user.passwd = m.hexdigest()
		user.email = request.POST['email']
		user.addtime = time.strftime('%Y%m%d%H%M',time.localtime())
		try:
			user.save()
			info = "注册成功"
			content = {'info':info}
			return render(request,'myweb/info.html',content)
		except:
			info = "注册失败"
	content = {'info':info}
	return render(request,'myweb/register.html',content)
#退出
def loginout(request):
	del request.session['userid']
	info = "退出成功"
	content = {'info':info}
	return render(request,'myweb/info.html',content)
