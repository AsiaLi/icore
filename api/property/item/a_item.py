# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

class AItem(api_resource.ApiResource):
    """
    财产科目
    """
    app = 'property'
    resource = 'item'

    @param_required(['user', 'name:str', 'remark:str'])
    def put(args):
        pass

