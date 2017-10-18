# -*- coding: utf-8 -*-

class Config(object):
	def __init__(self, keys):
		self.key_set = set(keys)

	def __getattr__(self, name):
		if name in self.key_set:
			return name.lower()
		else:
			return None

ORDER = Config([
	'CONFIRM_DELIVERY_ITEM', #商户确认发货单
	'COMPLETE_PAY_ORDER', #完成订单支付
	'COMPLETE_ORDER', #完成订单
	'CREATE_ORDER', #创建订单
	'REFUND_DELIVERY_ITEM', #申请退款
	'REQUEST_PLATFORM_REFUND', #申请平台操作退款
	'REJECT_REFUND', #驳回退款申请
])

PRODUCT = Config([
	'CREATE_PRODUCT', #创建商品
])

MEMBER = Config([
	'CREATE_CUSTOM_MEMBER_GRADE', #创建自定义会员等级(非自动升级)
])

if __name__ == '__main__':
	print ORDER.CONFIRM_DELIVERY_ITEM
	print ORDER.COMPLETE_PAY_ORDER