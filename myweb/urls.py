"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views,viewsorders,viewsusers

urlpatterns = [
    #=====================登录注册退出===================================
    #主页
	url(r'^$',views.index,name="index"),
    #全部商品页
	url(r'^goodslist(?P<typeid>[0-9]*)$',views.goodslist,name="goodslist"),
    #详情页
    url(r'^information(?P<goodsid>[0-9]+)$',views.information,name="information"),
    #登录
    url(r'^login$',views.login,name="login"),
    #验证码
    url(r'^verify$',views.verify,name="verify"),
    #执行登录
    url(r'^dologin$',views.dologin,name="dologin"),
    #注册
    url(r'^register$',views.register,name="register"),
    #执行注册
    url(r'^doregister$',views.doregister,name="doregister"),
    #退出
    url(r'^loginout$',views.loginout,name="loginout"),
    #=====================end 登录注册退出===================================

    #=====================订单和购物车操作==============================
    #添加购物车
    url(r'^cartadd$',viewsorders.cartadd,name="cartadd"),
    #浏览购物车
    url(r'^cartshow$',viewsorders.cartshow,name="cartshow"),
    #购物车删除商品
    url(r'^cartgdel$',viewsorders.cartgdel,name="cartgdel"),
    #购物车清空
    url(r'^cartclaer$',viewsorders.cartclaer,name="cartclaer"),
    #购物车商品数量改变
    url(r'^cartgchan$',viewsorders.cartgchan,name="cartgchan"),
    #结算购物车,即添加订单
    url(r'^orderadd$',viewsorders.orderadd,name="orderadd"),
    #订单确认
    url(r'^orderconfirm$',viewsorders.orderconfirm,name="orderconfirm"),
    #订单已确认
	url(r'^ordersure$',viewsorders.ordersure,name="ordersure"),
    #=====================end 订单和购物车操作==============================

    #=====================个人主页信息==========================================
    #个人
    url(r'^userinfo$',viewsusers.userinfo,name="userinfo"),
    #个人信息修改
    url(r'^usinfoch$',viewsusers.usinfoch,name="usinfoch"),
    #执行个人信息修改
    url(r'^dousinfoch$',viewsusers.dousinfoch,name="dousinfoch"),
    #密码重置
    url(r'^passwdreset$',viewsusers.passwdreset,name="passwdreset"),
    #执行密码重置
    url(r'^dopwreset$',viewsusers.dopwreset,name="dopwreset"),
    #收货地址管理
    url(r'^addressmange$',viewsusers.addressmange,name="addressmange"),
    #地址级联
    url(r'^district(?P<upid>[0-9]+)$',viewsusers.district,name="district"),
    #保存地址
    url(r'^saveaddr$',viewsusers.saveaddr,name="saveaddr"),
    #订单浏览
    url(r'^orderviews(?P<pIndex>[0-9]*)$',viewsusers.orderviews,name="orderviews"),
    #查看订单详情
    url(r'^orderdetail$',viewsusers.orderdetail,name="orderdetail"),
    #取消订单
    url(r'^ordercancel$',viewsusers.ordercancel,name="ordercancel"),
    #=====================end 个人主页信息==========================================
]
