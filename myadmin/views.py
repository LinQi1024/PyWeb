from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from myadmin.models import Users,District
from django.core.paginator import Paginator
import time,hashlib
from django.core.urlresolvers import reverse
#====================后台登录=================================
#返回登录页页面
def login(request):
	return render(request,'myadmin/login.html')

#验证登录信息
def dologin(request):
	vc1 = request.POST['verifycode'].lower()
	vc2 =request.session['verifycode'].lower()
	if vc1 != vc2:
		info = "验证码错误"
		content = {'info':info}
		return render(request,'myadmin/login.html',content)
	try:
		user = Users.objects.get(username=request.POST['username'])
		passwd1 = request.POST['passwd']
		m = hashlib.md5()
		m.update(bytes(passwd1,encoding="utf8"))
		passwd2 = m.hexdigest()
		if passwd2 == user.passwd and user.state==0:
			request.session['adminuser'] = user.name
			content = {'name':user.name}
			return render(request,'myadmin/index.html',content)
		else:
			info = "账号密码错误"
	except:
		info = "账号密码错误"
	content = {'info':info}
	return render(request,'myadmin/login.html',content)

#返回验证码
def verify(request):
	#引入随机函数模块
	import random
	from PIL import Image, ImageDraw, ImageFont
	#定义变量，用于画面的背景色、宽、高
	#bgcolor = (random.randrange(20, 100), random.randrange(
	#    20, 100),100)
	bgcolor = (242,164,247)
	width = 100
	height = 25
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

#退出登录
def logout(request):
	del request.session['adminuser']
	return redirect(reverse('myadmin_login'))
#====================end后台登录=================================

#后台主页
def index(request):
	name = request.session['adminuser']
	content = {'name':name}
	return render(request,'myadmin/index.html',content)

#=======================会员管理=================================
#会员浏览
def usersshow(request,pIndex):
	userslist = Users.objects.filter()
	p = Paginator(userslist, 5)
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
	name = request.session['adminuser']
	content = {'userslist':list2,'plist':plist,'pIndex':pIndex,'name':name,'previous':previous,'next':next}
	return render(request,'myadmin/users/usersshow.html',content)

#会员添加
def usersadd(request):
	name = request.session['adminuser']
	content = {'name':name}
	return render(request,'myadmin/users/usersadd.html',content)
#执行添加操作
def usersinsert(request):
	user = Users()
	user.username = request.POST['username']
	user.name = request.POST['name']
	m = hashlib.md5()
	m.update(bytes(request.POST['passwd'],encoding="utf8"))
	user.passwd = m.hexdigest()
	user.sex = request.POST['sex']
	addresslist = request.POST.getlist('district')
	addressdetail = request.POST['address']
	user.address = ' '.join(addresslist) + ' ' + addressdetail
	user.code = request.POST['code']
	user.phone = request.POST['phone']
	user.email = request.POST['email']
	user.state = request.POST['state']
	user.addtime = time.strftime('%Y%m%d%H%M',time.localtime())
	try:
		user.save()
		info = '添加成功'
	except:
		info = '添加失败'
	name = request.session['adminuser']
	content = {'info':info,'name':name}
	return render(request,'myadmin/info.html',content)
# 加载对应的城市信息，并json格式ajax方式响应
def district(request,upid):
    dlist = District.objects.filter(upid=upid)
    list1 = []
    for ob in dlist:
        list1.append({'id':ob.id,'name':ob.name})
    return JsonResponse({'data':list1})

#会员修改
def usersedit(request,userid):
	userslist = Users.objects.filter(id=userid)
	name = request.session['adminuser']
	content = {'userslist':userslist,'name':name}
	return render(request,'myadmin/users/usersedit.html',content)
#执行修改操作
def usersupdate(request):
	user = Users.objects.get(id=request.POST['id'])
	user.name = request.POST['name']
	m = hashlib.md5()
	m.update(bytes(request.POST['passwd'],encoding="utf8"))
	user.passwd = m.hexdigest()
	user.sex = request.POST['sex']
	user.address = request.POST['address']
	user.code = request.POST['code']
	user.phone = request.POST['phone']
	user.email = request.POST['email']
	user.state = request.POST['state']
	try:
		user.save()
		info = '修改成功'
	except:
		info = '修改失败'
	name = request.session['adminuser']
	content = {'info':info,'name':name}
	return render(request,'myadmin/info.html',content)

#会员删除
def usersdel(request,userid):
	users = Users.objects.get(id=userid)
	try:
		users.delete()
		info = '删除成功'
	except:
		info = '删除失败'
	name = request.session['adminuser']
	content = {'info':info,'name':name}
	return render(request,'myadmin/info.html',content)
#=======================end会员管理=================================