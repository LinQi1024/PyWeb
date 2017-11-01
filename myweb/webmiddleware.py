#自定义后台中间件
import re
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
class WebMiddleware(object):
	def __init__(self,get_response):
		self.get_response = get_response
		
	def __call__(self,request):
		pathlist = ["/","/login","/verify","/dologin","/register","/doregister","/loginout"]
		# 判断当前请求 不是后台网站 不是商品列表页 不是商品详情页 以及不在上述列表中
		if (not re.match("/myadmin",request.path)) and (not re.match("/goodslist",request.path)) and (not re.match("/information",request.path)) and (request.path not in pathlist):
			#判断是否已登录
			if "userid" not in request.session:
				return redirect(reverse('login'))
		response = self.get_response(request)
		return response