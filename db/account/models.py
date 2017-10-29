#coding: utf8
from rust.core import base_db_models as models

import datetime

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

class UserProfile(models.Model):
	"""
	用户profile
	"""
	user = models.ForeignKey(User)
	is_active = models.BooleanField(default=True, verbose_name='用户是否有效')
	note = models.TextField(default='')
	status = models.IntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	class Meta(object):
		db_table = 'account_user_profile'