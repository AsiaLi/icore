# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

class AUserItems(api_resource.ApiResource):
    """
    用户持有的财产科目列表
    """
    app = 'property'
    resource = 'user_items'

    @param_required(['user'])
    def get(args):
        pass

