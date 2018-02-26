# -*- coding: utf-8 -*-

import os
import sys

path = os.path.abspath(os.path.join('.', '..'))
sys.path.insert(0, path)

import unittest
import settings
from features.util import bdd_util


if settings.DATABASES['default']['HOST'] != 'db.home.com':
	raise RuntimeError("Do not run BDD when connect online database")

######################################################################################
# __clear_all_account_data: 清空账号数据
######################################################################################
def __clear_all_account_data():
	pass


######################################################################################
# __clear_all_app_data: 清空应用数据
######################################################################################
clean_modules = []
def __clear_all_app_data():
	"""
	清空应用数据
	"""
	if len(clean_modules) == 0:
		for clean_file in os.listdir('./features/clean'):
			if clean_file.startswith('__'):
				continue

			module_name = 'features.clean.%s' % clean_file[:-3]
			module = __import__(module_name, {}, {}, ['*',])	
			clean_modules.append(module)

	for clean_module in clean_modules:
		clean_module.clean()

def __clear_pre_account_data():
	"""
	清空默认创建的帐号
	"""
	pass

def before_all(context):
	#cache_utils.clear_db()

	#创建test case，使用assert
	context.tc = unittest.TestCase('__init__')
	bdd_util.tc = context.tc

	#设置bdd模式
	settings.IS_UNDER_BDD = True
	settings.DUMP_API_CALL_RESULT = False
	settings.ENABLE_BDD_DUMP_RESPONSE = False

def after_all(context):
	pass


def before_scenario(context, scenario):
	context.scenario = scenario
	__clear_all_app_data()
	__clear_pre_account_data()

def after_scenario(context, scenario):
	if hasattr(context, 'client') and context.client:
		context.client.logout()