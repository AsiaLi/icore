#coding: utf8

from rust.core import base_db_models as models

MEMBER_ROLE = {
	'GDAD': 0,
	'GMUM': 1,
	'DAD': 2,
	'MUM': 3,
	'SON': 4,
	'DAT': 5,
}

class Member(models.Model):
	"""
	家庭成员
	"""
	name = models.CharField(max_length=30)
	role = models.IntegerField(MEMBER_ROLE['DAD'])
	email = models.EmailField(default='')
	phone = models.CharField(default='')
	is_active = models.BooleanField(default=True)
	is_super = models.BooleanField(default=False)
	password = models.CharField(max_length=120)
	created_at = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'member_member'