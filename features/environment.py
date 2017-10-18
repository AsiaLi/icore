# -*- coding: utf-8 -*-

import os
import sys

path = os.path.abspath(os.path.join('.', '..'))
sys.path.insert(0, path)

import unittest
import settings
from features.util import bdd_util
from features.util import account_util 
from eaglet.core.cache import utils as cache_utils


if settings.DATABASES['default']['HOST'] != 'db.dev.com':
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
	account_util.account_models.UserProfile.delete().dj_where(user_id__gt=6).execute()
	account_util.account_models.User.delete().dj_where(id__gt=6).execute()

def before_all(context):
	#cache_utils.clear_db()

	#创建test case，使用assert
	context.tc = unittest.TestCase('__init__')
	bdd_util.tc = context.tc

	#设置bdd模式
	settings.IS_UNDER_BDD = True
	settings.DUMP_FORMATTED_INNER_ERROR_MSG = True
	settings.DUMP_API_CALL_RESULT = False
	settings.ENABLE_BDD_DUMP_RESPONSE = False

	#创建测试账户
	account_util.create_platform_corp('weizoom')
	account_util.create_supplier_corp('jobs').connect_platform('weizoom')
	account_util.create_supplier_corp('bill').connect_platform('weizoom')
	account_util.create_supplier_corp('tom').connect_platform('weizoom')
	account_util.create_supplier_corp('lucy').connect_platform('weizoom')
	account_util.create_platform_corp('njnarong')

def after_all(context):
	pass


def before_scenario(context, scenario):
	context.scenario = scenario
	__clear_all_app_data()
	__clear_pre_account_data()
	# 创建平台下的普通商圈
	account_util.create_super_group()
	account_util.create_member('weizoom', 'zhouxun', u'周迅')
	account_util.create_member('weizoom', 'yangmi', u'杨幂')
	account_util.create_member('weizoom', 'baby', u'AngelaBaby')

def after_scenario(context, scenario):
	if hasattr(context, 'client') and context.client:
		context.client.logout()

	# if hasattr(context, 'driver') and context.driver:
	# 	print('[after scenario]: close browser driver')
	# 	page_frame = PageFrame(context.driver)
	# 	page_frame.logout()
	# 	context.driver.quit()

	if hasattr(context, 'webapp_driver') and context.driver:
		print('[after scenario]: close webapp browser driver')
		context.webapp_driver.quit()

