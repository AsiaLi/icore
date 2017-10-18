# -*- coding: utf-8 -*-

def ParamObject(data):
	"""
	构建不可变属性对象
	"""

	class Inner(object):
		__slots__ = tuple(data.keys())

		def __init__(self, dict_data):
			for k, v in dict_data.items():
				setattr(self, k, v)

	return Inner(data)