#coding: utf8

from rust.core import base_db_models as models

class Item(models.Model):
	"""
	财产科目
	"""
	name = models.CharField(max_length=64, default='')
	remark = models.CharField(max_length=1024, default='')

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'property_item'

class UserHasPropertyItem(models.Model):
	"""
	用户持有的财产科目
	"""
	user_id = models.IntegerField(default=0)
	name = models.CharField(max_length=1024, default='')
	money = models.FloatField(default=0)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'user_has_property_item'