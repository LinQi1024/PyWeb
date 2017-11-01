from django.db import models

#用户信息users表
class Users(models.Model):
	username = models.CharField(max_length=32)
	name = models.CharField(max_length=16)
	passwd = models.CharField(max_length=32)
	sex = models.IntegerField()
	address = models.CharField(max_length=255)
	code = models.CharField(max_length=6)
	phone = models.CharField(max_length=16)
	email = models.CharField(max_length=50)
	state = models.IntegerField(default=1)
	addtime = models.IntegerField()
	class Meta:
		db_table = "myadmin_users"

#商品信息
class Goods(models.Model):
	typeid = models.IntegerField()
	goods = models.CharField(max_length=32)
	company = models.CharField(max_length=50)
	descr = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	picname = models.CharField(max_length=255)
	state = models.IntegerField(default=1)
	store = models.IntegerField(default=0)
	num = models.IntegerField(default=0)
	clicknum = models.IntegerField(default=0)
	addtime = models.IntegerField()
	class Meta:
		db_table = "myadmin_goods"
	def toDict(self):
		return {'goodsid':self.id,'goods':self.goods,'descr':self.descr,'price':self.price,'picname':'l'+self.picname,'store':self.store}

#商品类别
class Type(models.Model):
	name = models.CharField(max_length=32)
	pid = models.IntegerField(default=0)
	path = models.CharField(max_length=255)
	class Meta:
		db_table = "myadmin_type"

#订单表
class Orders(models.Model):
	uid = models.IntegerField()
	linkman =  models.CharField(max_length=32)
	address = models.CharField(max_length=255)
	code = models.CharField(max_length=6)
	phone = models.CharField(max_length=16)
	addtime = models.IntegerField()
	total = models.DecimalField(max_digits=8, decimal_places=2,default=0.00)
	status = models.IntegerField(default=1)
	class Meta:
		db_table = "myadmin_orders"

#订单详情
class Detail(models.Model):
	orderid =  models.IntegerField()
	goodsid = models.IntegerField()
	name = models.CharField(max_length=32)
	price =  models.DecimalField(max_digits=6, decimal_places=2,default=0.00)
	num = models.IntegerField(default=0)
	class Meta:
		db_table = "myadmin_detail"
	def toDict(self):
		return {'goodsid':self.goodsid,'name':self.name,'price':self.price,'num':self.num}

#城市信息表
class District(models.Model):
	name = models.CharField(max_length=255)
	upid = models.IntegerField()
	class Meta:
		db_table = "myadmin_district"
