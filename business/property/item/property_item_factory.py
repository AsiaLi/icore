# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.business import Service
from rust.core.exceptionutil import BusinessError

from business.property.item.property_item import PropertyItem
from db.property import models as property_models

class PropertyItemFactory(Service):

    def create(self, param_object):
        existed_model = property_models.PropertyItem.select().where(
            property_models.PropertyItem.name == param_object.name
        ).first()
        if existed_model:
            raise BusinessError('already exist')
        db_model = property_models.PropertyItem.create(
            name = param_object.name,
            remark = param_object.remark,
            group = param_object.group
        )
        return PropertyItem(db_model)

    def update(self, param_object):
        property_models.PropertyItem.update(
            name = param_object.name,
            remark = param_object.remark
        ).where(property_models.PropertyItem.id == param_object.id).execute()

    def delete(self, property_item_id):
        pass