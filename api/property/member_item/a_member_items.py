# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

class AMemberItems(api_resource.ApiResource):
    """
    用户持有的财产科目列表
    """
    app = 'property'
    resource = 'member_items'

    @param_required(['member'])
    def get(args):
        pass

