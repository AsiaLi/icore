# -*- coding: utf-8 -*-

import logging

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(filename)s - %(message)s')

IS_REGISTER_STRATEGIES = False

class RegisterSystemStrategyMiddleware(object):
	"""
	目前没有合适的位置对strategy进行初始化，放在middleware中
	TODO: 在eaglet中加入app.create_app时间点的hook机制
	"""
	def process_request(sel, req, resp):
		global IS_REGISTER_STRATEGIES
		if not IS_REGISTER_STRATEGIES:
			IS_REGISTER_STRATEGIES = True    

			import settings
			for module, strategies in settings.STRATEGIES.items():
				for strategy in strategies:
					module_name = strategy
					module = __import__(module_name, {}, {}, ['*',])
					logging.info('register %s' % strategy)		