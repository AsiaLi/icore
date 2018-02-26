#coding: utf8

from rust.core.event import event_handler
from settings import DOMAIN_EVENTS as events

@event_handler(events.PROPERTY.ITEM.CREATED)
def handler(data):
	print 'property item created'
	pass