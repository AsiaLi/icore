# -*- coding: utf-8 -*-
from datetime import datetime
import logging

from rust.core import business

INSTANCE = None

class EventBus(business.Service):
	"""
	同步状态
	发送消息的服务
	"""
	@classmethod
	def get(cls):
		global INSTANCE
		if not INSTANCE:
			INSTANCE = cls(None, None)
		
		return INSTANCE

	def __init__(self, corp, member):
		business.Service.__init__(self, corp, member)
		self.event2handlers = {}

	def register(self, event, handler):
		"""
		注册一个event的handler
		"""
		self.event2handlers.setdefault(event, []).append(handler)

	def send(self, event, data):
		"""
		发送一个event
		"""
		handlers = self.event2handlers.get(event)
		if not handlers:
			logging.warn('no handlers for event "%s"' % event)
			return

		data['_time'] = datetime.now().strftime('%Y%m%d%H%M%S')
		for handler in handlers:
			handler(event, data)

def event_handler(event):
	"""
	使用event_handler向EventBus注册事件处理器

	@event_handler('event1')
	def event1_handler(event, data):
		...
		pass
	"""
	def wrapper(function):
		function.__name__ = '%s__%s' % (function.__module__, event)
		EventBus.get().register(event, function)	

	return wrapper