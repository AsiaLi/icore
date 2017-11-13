# -*- coding: utf-8 -*-
from business.property.item.property_item_repository import PropertyItemRepository
from business.property.item.property_item_service import PropertyItemService

__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

class AItems(api_resource.ApiResource):
    """
    财产科目列表
    """
    app = 'property'
    resource = 'items'

    @param_required(['member_id'])
    def get(args):
        member = args['member']
        property_items = PropertyItemRepository(member).get_property_items()
        property_group, expense_group, income_group = PropertyItemService().split_by_group(property_items)
        return {
            'property_group': [{
                'id': item.id,
                'name': item.name,
                'group': item.group_name,
            } for item in property_group],
            'expense_group': [{
                'id': item.id,
                'name': item.name,
                'group': item.group_name,
            } for item in expense_group],
            'income_group': [{
                'id': item.id,
                'name': item.name,
                'group': item.group_name,
            } for item in income_group]
        }