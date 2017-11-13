#coding: utf8

from rust.core import base_db_models as models

class Family(models.Model):
	"""
	家庭信息
	"""
	name = models.CharField(max_length=30)
	manager_id = models.IntegerField(default=0)
	address = models.CharField(default='', max_length=2048)
	phone = models.CharField(default='')
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'family_family'