# -*- coding: utf-8 -*-

class Model(object):
	"""
	领域业务对象的基类
	"""
	__slots__ = ('context', )
	
	def __init__(self):
		self.context = {}

		for slot in self.__slots__:
			#watchdog.info("setting '%s'" % slot)
			setattr(self, slot, None)

	def _init_slot_from_model(self, model, slots=None):
		if not slots:
			slots = self.__slots__

		for slot in slots:
			value = getattr(model, slot, None)
			if value != None:
				if 'id' == slot:
					value = int(value)
				setattr(self, slot, value)
			else:
				setattr(self, slot, None)

	def after_from_dict(self):
		"""
		from_dict调用结束前的hook函数，允许sub class修改from_dict的结果
		"""
		pass

	@classmethod
	def from_dict(cls, dict, slots=None):
		instance = cls()
		if not slots:
			slots = cls.__slots__

		for slot in slots:
			value = dict.get(slot, None)

			setattr(instance, slot, value)
		instance.after_from_dict()
		return instance

	def to_dict(self, *extras, **kwargs):
		result = dict()
		if kwargs and 'slots' in kwargs:
			slots = kwargs['slots']
		else:
			slots = self.__slots__

		for slot in slots:
			result[slot] = getattr(self, slot, None)

		if extras:
			for item in extras:
				result[item] = getattr(self, item, None)
			
		return result


class Service(object):
	"""
	领域服务的基类
	"""
	__slots__ = ('context', 'corp', 'webapp_user', 'member')

	@classmethod
	def get(cls):

		return cls()
	
	def __init__(self, corp=None, webapp_user=None):
		self.context = {
			'corp': corp,
			'webapp_user': webapp_user,
			'member': webapp_user
		}
		self.corp = corp
		self.webapp_user = webapp_user
		self.member = webapp_user


RESOURCE_TYPE_INTEGRAL = 'integral'
RESOURCE_TYPE_COUPON = 'coupon'
RESOURCE_TYPE_PRODUCT = 'product'
RESOURCE_TYPE_PRODUCTS = 'products'
class Resource(object):
	"""
	交易中的资源
	"""
	__slots__ = (
		'context',
		'priority' #资源处理的优先级
	)

	def __init__(self):
		self.context = {}

	def get_type(self):
		"""
		获得资源类型
		"""
		raise NotImplementedError

	def get_deduction_money(self):
		"""
		获得资源抵扣的金额
		"""
		raise NotImplementedError