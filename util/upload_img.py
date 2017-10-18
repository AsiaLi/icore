# -*- coding: utf-8 -*-

import base64
import time
from datetime import datetime
import os
try:
	from PIL import Image
except:
	import Image

import settings

########################################################################
# save_base64_img_file_local_for_webapp: 存储手机上传的图片
########################################################################
def save_base64_img_file_local(owner_id, ajax_file):
	date = time.strftime('%Y%m%d')
	dir_path_suffix = 'webapp/%d_%s' % (owner_id, date)
	dir_path = os.path.join(settings.UPLOAD_DIR, dir_path_suffix)

	if not os.path.exists(dir_path):
		os.makedirs(dir_path)

	#获取文件的扩展名
	file_name = '%s.%s' % (datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f"), 'png')
	ajax_path = '%s/%s' % (dir_path, file_name)
	ajax_file = ajax_file.split(',')

	image_content = base64.b64decode(ajax_file[1])
	image_file = open(ajax_path, 'wb')
	image_file.write(image_content)
	image_file.close()

	return '/static/upload/%s/%s' % (dir_path_suffix, file_name)


########################################################################
# __validate_image: 检查上传的文件格式是否正确
########################################################################
def __validate_image(path):
	try:
		im = Image.open(path)
		im.load()
		return True
	except:
		import sys
		import traceback
		type, value, tb = sys.exc_info()
		print type
		print value
		traceback.print_tb(tb)
		if 'image file is truncated' in str(value):
			return False
		else:
			return False