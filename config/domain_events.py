#coding: utf8

#领域事件处理
DOMAIN_EVENT_HANDLERS = {
    'PROPERTY_ITEM.CREATED': [
		'business.property.item.events.item_created',
	]
}

class __EventsObject(object):
	pass

"""
将字符串如'PROJECT.CREATED'转换成对象写法,
外部调用则变成events.PRODUCT.CREATED, 值为'PROJECT.CREATED'
"""
DOMAIN_EVENTS = __EventsObject()
for event, module_paths in DOMAIN_EVENT_HANDLERS.items():
	k1, k2 = event.split('.')
	if not hasattr(k1, DOMAIN_EVENTS):
		k1_c = __EventsObject()
		setattr(DOMAIN_EVENTS, k1, k1_c)
	else:
		k1_c = getattr(DOMAIN_EVENTS, k1)
	setattr(k1_c, k2, event)