# -*- coding: utf-8 -*-

class Config(object):
	def __init__(self, keys):
		self.key_set = set(keys)

	def __getattr__(self, name):
		if name in self.key_set:
			return name.lower()
		else:
			return None

MEMBER = Config([
	'CREATE_MEMBER', #创建会员
])