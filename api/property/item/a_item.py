# -*- coding: utf-8 -*-
from business.property.item.property_item_factory import PropertyItemFactory

__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

from api import ParamObject

class AItem(api_resource.ApiResource):
    """
    财产科目
    """
    app = 'property'
    resource = 'item'

    @param_required(['member_id', 'name:str', '?remark:str'])
    def get(args):
        return {
            'method': 'get',
            'list': [1, 2],
            'dict': {'a': 1, 'b': 2}
        }

    @param_required(['member_id', 'name:str', 'group:str', '?remark:str'])
    def put(args):
        member = args['member']
        if not member.is_manager():
            return 500, u'没有权限'

        param_object = ParamObject({
            'name': args['name'],
            'group': args['group'].upper(),
            'remark': args.get('remark', '')
        })
        item = PropertyItemFactory(member).create(param_object)
        return {
            'id': item.id
        }

    @param_required(['member_id', 'id:int', 'name:str', '?remark:str'])
    def post(args):
        member = args['member']
        if not member.is_manager():
            return 500, u'没有权限'

        param_object = ParamObject({
            'id': args['id'],
            'name': args['name'],
            'remark': args.get('remark', '')
        })
        PropertyItemFactory(member).update(param_object)
        return {}

    @param_required(['user_id', 'id:int'])
    def delete(args):
        pass

