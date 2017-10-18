# -*- coding: utf-8 -*-

import os
import inspect

from util.command import BaseCommand

from eaglet.core.db import models
import peewee

class Command(BaseCommand):
	help = ""
	args = ''

	def handle(self, *args, **options):
		print 'syncdb: create table'
		db_models = []
		collected_tables = set()
		for root, dirs, files in os.walk('./db'):
			for f in files:
				if '__init__' in f:
					continue

				if f.endswith('.pyc'):
					continue

				if '.DS_Store' in f:
					continue

				file_path = os.path.join(root, f)
				module_name = file_path[2:-3].replace(os.path.sep, '.')
				print file_path, ' ', module_name
				module = __import__(module_name, {}, {}, ['*',])
				for key, value in module.__dict__.items():
					if inspect.isclass(value) and issubclass(value, models.Model) and value.__module__ == module.__name__:
						db_model = value
						db_table = db_model._meta.db_table
						if db_table not in get_existed_models():
							if db_table in collected_tables:
								print '[duplicate table]: ', db_table
							else:
								print 'collect model: %s' % key
								collected_tables.add(db_table)
								db_models.append(value)

		print 'create %d tables...' % len(db_models)
		peewee.create_model_tables(db_models)
		for dt in collected_tables:
			print 'created {} success !'.format(dt)


def get_existed_models():
	import settings
	import MySQLdb
	config = settings.DATABASES['default']
	db = MySQLdb.connect(config['HOST'], config['USER'], config['PASSWORD'], config['NAME'], port=int(config['PORT']))
	cursor = db.cursor()
	cursor.execute('show tables;')
	rows = cursor.fetchall()
	models = set()
	for row in rows:
		models.add(row[0])

	return list(models)