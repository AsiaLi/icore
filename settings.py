# -*- coding: utf-8 -*-

import os

PROJECT_HOME = os.path.dirname(os.path.abspath(__file__))

MODE = os.environ.get('MODE', 'develop')
DEBUG = (os.environ.get('_DEBUG', '0') == '1')
SERVICE_NAME = 'icore'

DB_HOST = os.environ.get('_DB_HOST', 'db.dev.com')
DB_NAME = os.environ.get('_DB_NAME', 'icore')
DB_USER = os.environ.get('_DB_USER', 'aix')
DB_PORT = os.environ.get('_DB_PORT', '3306')
DB_PASSWORD = os.environ.get('_DB_PASSWORD', 'aix')

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
    'middleware.account_middleware.AccountMiddleware',
]

#信息输出配置
DUMP_API_CALL_RESULT = True
ENABLE_CONSOLE = (os.environ.get('_ENABLE_API_CONSOLE', '1') == '1')
SERVICE_HOST = '127.0.0.1:8000'

UPLOAD_DIR = os.path.join(PROJECT_HOME, 'static', 'upload')  # 文件上传路径
UPLOAD_HTTP_PATH = '/static/upload'

#无需经过中间件的资源
DIRECT_PATHS = [
    '/static/',
    '/console',
    '/logined_user/',
]

RUST_RESOURCES = [
    'test',
    'user',
    'permission',
]

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