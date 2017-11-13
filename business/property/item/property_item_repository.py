# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.business import Service

from business.property.item.property_item import PropertyItem
from db.property import models as property_models

class PropertyItemRepository(Service):

    def get_property_items(self):
        db_models = property_models.PropertyItem.select().where(
            property_models.PropertyItem.is_deleted == False
        )
        return [PropertyItem(model) for model in db_models]


