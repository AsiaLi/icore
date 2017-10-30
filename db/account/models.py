#coding: utf8

from rust.core import base_db_models as models

class User(models.Model):
	"""
	从django.contrib.auth.User迁移过来
	"""
	username = models.CharField(max_length=30)
	email = models.EmailField(default='')
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	password = models.CharField(max_length=120)
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'auth_user'

class UserProfile(models.Model):
	"""
	用户profile
	"""
	user_id = models.IntegerField(default=0)
	manager_id = models.IntegerField(default=0)
	nick_name = models.CharField(default='')
	phone = models.CharField(max_length=20, default='')
	birthday = models.DateTimeField()
	remark = models.TextField(default='')
	status = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta(object):
		db_table = 'account_user_profile'