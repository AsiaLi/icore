# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

class AUserItem(api_resource.ApiResource):
    """
    用户持有的财产科目
    """
    app = 'property'
    resource = 'user_item'

    @param_required(['user', 'name:str', 'remark:str'])
    def put(args):
        pass

