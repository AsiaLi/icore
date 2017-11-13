# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.business import Service

from db.property import models as property_models

class PropertyItemService(Service):

    def split_by_group(self, items):
        property_groups = []
        expense_groups = []
        income_group = []

        for item in items:
            if item.group == property_models.PROPERTY_ITEM_GROUP['PROPERTY']:
                property_groups.append(item)
            elif item.group == property_models.PROPERTY_ITEM_GROUP['EXPENSE']:
                expense_groups.append(item)
            elif item.group == property_models.PROPERTY_ITEM_GROUP['INCOME']:
                income_group.append(item)
        return property_groups, expense_groups, income_group