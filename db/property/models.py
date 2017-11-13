#coding: utf8

from rust.core import base_db_models as models

PROPERTY_ITEM_GROUP = {
	'PROPERTY': 0, #财产
	'EXPENSE': 1, #消费
	'INCOME': 2, #收入
}

PROPERTY_ITEM_GROUP2TEXT = ['PROPERTY', 'EXPENSE', ]

class PropertyItem(models.Model):
	"""
	财产科目
	"""
	name = models.CharField(max_length=64, default='')
	remark = models.CharField(max_length=1024, default='')
	group = models.IntegerField(default=PROPERTY_ITEM_GROUP['PROPERTY']) #科目组别

	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'property_item'

class MemberHasPropertyItem(models.Model):
	"""
	用户持有的财产科目
	"""
	member_id = models.IntegerField(default=0)
	property_item_id = models.IntegerField(default=0)
	remark = models.CharField(max_length=1024, default='')
	balance = models.FloatField(default=0)

	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'member_has_property_item'