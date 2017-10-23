# -*- coding: utf-8 -*-

import os
import logging

PROJECT_HOME = os.path.dirname(os.path.abspath(__file__))

MODE = os.environ.get('_SERVICE_MODE', 'develop')
DEBUG = MODE == 'develop'
DEV_SERVER_MULTITHREADING = False

DB_NAME = os.environ.get('DB_NAME', 'test')
DB_USER = os.environ.get('DB_USER', 'test')
DB_HOST = os.environ.get('DB_HOST', 'test')
DB_PORT = os.environ.get('DB_PORT', '3333')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'test')

print os.environ

DATABASES = {
    'default': {
        'ENGINE': 'mysql+retry',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'CONN_MAX_AGE': 100
    }
}

MIDDLEWARES = [

]

#信息输出配置
ENABLE_CONSOLE = os.environ.get('_ENABLE_API_SERVICE_CONSOLE', '0') == '1'

# settings for WAPI Logger
if 'develop' == MODE:
    ENABLE_SQL_LOG = False #是否dump peewee产生的sql查询
    DUMP_API_CALL_RESULT = True
    DUMP_FORMATTED_INNER_ERROR_MSG = True
    SERVICE_HOST = '127.0.0.1:8000'
else:
    ENABLE_SQL_LOG = False #是否dump peewee产生的sql查询
    DUMP_API_CALL_RESULT = False
    DUMP_FORMATTED_INNER_ERROR_MSG = False
    SERVICE_HOST = None


UPLOAD_DIR = os.path.join(PROJECT_HOME, 'static', 'upload')  # 文件上传路径
UPLOAD_HTTP_PATH = '/static/upload'

def load_custom_configs():
    configs = {}
    attr2file = {}
    for f in os.listdir('./config'):
        if f.startswith('__init'):
            continue

        if f.endswith('.py'):
            module_part = f[0:-3]
            module_name = 'config.{}'.format(module_part)
            module = __import__(module_name, {}, {}, ['*',])
            for attr in module.__dict__.keys():
                if attr.startswith('__'):
                    continue

                if attr in configs:
                    print '[WARN]: settings.%s(%s) is already defined in `%s`' % (attr, f, attr2file[attr])
                configs[attr] = getattr(module, attr)
                attr2file[attr] = f

    return configs            

locals().update(load_custom_configs())
