
from django.conf.urls import url
#后台主页视图
from . import views
#后台商品类别和信息视图
from . import viewsgoods
#后台订单视图
from . import viewsorders

urlpatterns = [
	
	#管理员登录路由
	url(r'^login$',views.login,name="myadmin_login"),
	url(r'^dologin$',views.dologin,name="myadmin_dologin"),
	url(r'^logout$',views.logout,name="myadmin_logout"),
	url(r'^verify$',views.verify,name="myadmin_verify"),

	#后台主页路由
	url(r'^$',views.index,name="myadmin_index"),

	#====================会员管理路由===========================
	#会员浏览
	url(r'^usersshow(?P<pIndex>[0-9]*)$',views.usersshow,name="myadmin_usersshow"),
	
	#会员添加
	url(r'^usersadd$',views.usersadd,name="myadmin_usersadd"),
	url(r'^usersinsert$',views.usersinsert,name="myadmin_usersinsert"),
	url(r'^district/([0-9]+)$', views.district, name='myadmin_district'),
	
	#会员修改
	url(r'^usersedit(?P<userid>[0-9]+)$',views.usersedit,name="myadmin_usersedit"),
	url(r'^usersupdate$',views.usersupdate,name="myadmin_usersupdate"),
	
	#会员删除
	url(r'^usersdel(?P<userid>[0-9]+)$',views.usersdel,name="myadmin_usersdel"),
	#====================end会员管理路由===========================

	#====================商品类别管理路由===========================
	#商品类别浏览
	url(r'^typeshow$',viewsgoods.typeshow,name="myadmin_typeshow"),
	
	#商品类别添加
	url(r'^typeadd$',viewsgoods.typeadd,name="myadmin_typeadd"),
	url(r'^typeinsert$',viewsgoods.typeinsert,name="myadmin_typeinsert"),
	
	#商品类别修改
	url(r'^typeedit(?P<typeid>[0-9]+)$',viewsgoods.typeedit,name="myadmin_typeedit"),
	url(r'^typeupdate$',viewsgoods.typeupdate,name="myadmin_typeupdate"),
	
	#商品类别删除
	url(r'^typedel(?P<typeid>[0-9]+)$',viewsgoods.typedel,name="myadmin_typedel"),
	#====================end商品类别管理路由===========================

	#====================商品信息管理路由===========================
	#商品浏览
	url(r'^goodsshow(?P<pIndex>[0-9]*)$',viewsgoods.goodsshow,name="myadmin_goodsshow"),

	#商品添加
	url(r'^goodsadd$',viewsgoods.goodsadd,name="myadmin_goodsadd"),
	url(r'^goodsinsert$',viewsgoods.goodsinsert,name="myadmin_goodsinsert"),

	#商品修改
	url(r'^goodsedit(?P<goodsid>[0-9]+)$',viewsgoods.goodsedit,name="myadmin_goodsedit"),
	url(r'^goodsupdate$',viewsgoods.goodsupdate,name="myadmin_goodsupdate"),

	#商品删除
	url(r'^goodsdel(?P<goodsid>[0-9]+)$',viewsgoods.goodsdel,name="myadmin_goodsdel"),
	#====================end商品信息管理路由===========================

	#====================订单信息管理路由===========================
	#订单浏览
	url(r'^ordersshow(?P<pIndex>[0-9]*)$',viewsorders.ordersshow,name="myadmin_ordersshow"),

	#订单详情
	url(r'^ordersdetail(?P<orderid>[0-9]*)$',viewsorders.ordersdetail,name="myadmin_ordersdetail"),

	#修改订单状态
	url(r'^ordersupdate$',viewsorders.ordersupdate,name="myadmin_ordersupdate"),
	#====================end订单信息管理路由===========================
]
