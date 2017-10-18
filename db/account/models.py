#coding: utf8
from eaglet.core.db import models

import datetime

WEIZOOM_CORP_ID = 1127

class User(models.Model):
	"""
	从django.contrib.auth.User迁移过来
	"""
	username = models.CharField(max_length=30)
	first_name = models.CharField(max_length=30, default='')
	last_name = models.CharField(max_length=30, default='')
	email = models.EmailField(default='')
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	password = models.CharField(max_length=120)
	date_joined = models.DateTimeField(default=datetime.datetime.now)
	last_login = models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		db_table = 'auth_user'
		verbose_name = 'user'
		verbose_name_plural = 'users'

CORP_TYPE = {
	'PLATFORM': 2,
	'COMMUNITY': 1,
	'SUPPLIER': 4,
}

WEBAPP_TYPE_MALL = 0 #普通商城
WEBAPP_TYPE_WEIZOOM_MALL = 1 #微众商城
WEBAPP_TYPE_WEIZOOM = 2 #微众公司
WEBAPP_TYPE_PLATFORM = 2 #平台
WEBAPP_TYPE_MULTI_SHOP = 3 #多门店
WEBAPP_TYPE_SUPPLIER = 4 #供货商

class UserProfile(models.Model):
	"""
	用户profile
	"""
	user = models.ForeignKey(User)
	platform_ids = models.CharField(default=WEIZOOM_CORP_ID, max_length=128) #多平台corp_id，逗号分割
	manager_id = models.IntegerField(default=0) #创建该用户的系统用户的id
	webapp_id = models.CharField(max_length=16, default=0)
	webapp_type = models.IntegerField(default=0) #商城类型
	company_name = models.CharField(max_length=128, default='')
	app_display_name = models.CharField(max_length=50, verbose_name='用于显示app名称', default='')
	is_active = models.BooleanField(default=True, verbose_name='用户是否有效')
	note = models.TextField(default='')
	status = models.IntegerField(default=1)
	is_mp_registered = models.BooleanField(default=False, verbose_name='是否已经接入了公众账号')
	is_self_run_account = models.BooleanField(default=False) #是否是自营的账号
	mp_token = models.CharField(max_length=50, verbose_name='绑定公众号使用的token', default='')
	mp_url = models.CharField(max_length=256, verbose_name='公众号绑定的url', default='')
	webapp_template = models.CharField(max_length=50, default='shop') #webapp的模板
	is_customed = models.IntegerField(default=0) #是否客户自定义CSS样式：1：是；0：否
	is_under_previewed = models.IntegerField(default=0) #是否是预览模式：1：是；0：否
	expire_date_day = models.DateField(auto_now_add=True)
	force_logout_date = models.BigIntegerField(default=0)

	homepage_template_name = models.CharField(max_length=250, default='') #首页模板名
	backend_template_name = models.CharField(max_length=250, default='') #后端页面模板名
	homepage_workspace_id = models.IntegerField(default=0) #homepage workspace的id

	#wepage
	is_use_wepage = models.BooleanField(default=False) #是否启用wepage
	store_name = models.CharField(max_length=64, default="") #店铺名称
	#结算账期
	settlement_period = models.IntegerField(default=1)
	is_formal = models.BooleanField(default=True) #账户类型是否是正式账号
	kefu_url = models.CharField(max_length=256, default="") #客服url

	created_at = models.DateTimeField(auto_now_add=True)
	class Meta(object):
		db_table = 'account_user_profile'


class GaiaApp(models.Model):
	"""
	【Gaia用】GaiaApp
	"""
	name = models.CharField(max_length=20, db_index=True)
	app_key = models.CharField(max_length=50, unique=True)
	app_secret = models.CharField(max_length=50)
	is_deleted = models.BooleanField(default=False)

	class Meta(object):
		db_table = "gaia_app"


class AccessToken(models.Model):
	"""
	【Gaia用】存储access token （Weapp不应访问此库）
	"""
	access_token = models.CharField(max_length=50, unique=True) # unique implies the creation of an index
	corp_id = models.CharField(max_length=50, default='')
	used_count = models.IntegerField(default=0) # 使用过次数
	created_at = models.DateTimeField(auto_now_add=True)
	expire_time = models.DateTimeField() # 失效时间
	app = models.ForeignKey(GaiaApp)
	is_active = models.BooleanField(default=True)

	class Meta(object):
		db_table = "access_token"


class IdentifyingCode(models.Model):
	"""
	【Gaia用】存储手机号对应的验证码
	"""
	phone = models.CharField(max_length=30, db_index=True)
	code = models.CharField(max_length=10, default='')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta(object):
		db_table = "identifying_code"


class ImoneySetting(models.Model):
	"""
	虚拟货币的配置信息
	"""
	corp_id = models.IntegerField(default=0)
	name = models.CharField(default='') #虚拟货币的名称，比如书宝宝
	set_rmb = models.FloatField(default=1) #兑换设置
	set_imoney = models.FloatField(default=1) #兑换设置
	status = models.BooleanField(default=True) #是否可用

	class Meta(object):
		db_table = "imoney_setting"