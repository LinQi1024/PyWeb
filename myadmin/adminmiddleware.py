#自定义后台中间件
import re
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
class AdminMiddleware(object):
	def __init__(self,get_response):
		self.get_response = get_response
		
	def __call__(self,request):
		pathlist = ["/myadmin/login","/myadmin/dologin","/myadmin/logout","/myadmin/verify"]
		# 判断当前请求是否是访问的网站后台以及请求不是登录,执行登录,验证码和退出登录
		if re.match("/myadmin",request.path) and (request.path not in pathlist):
			#判断是否已登录
			if "adminuser" not in request.session:
				return redirect(reverse('myadmin_login'))
		response = self.get_response(request)
		return response