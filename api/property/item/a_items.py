# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

class AItems(api_resource.ApiResource):
    """
    财产科目列表
    """
    app = 'property'
    resource = 'items'

    @param_required(['user'])
    def get(args):
        pass

