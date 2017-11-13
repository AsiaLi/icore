# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.business import Model

from db.property import models as property_models

class PropertyItem(Model):

    __slots__ = (
        'id',
        'name',
        'remark',
        'group',
        'is_deleted',
    )

    def __init__(self, db_model):
        Model.__init__(self)
        if db_model:
            self._init_slot_from_model(db_model)

    @property
    def group_name(self):
        return property_models.PROPERTY_ITEM_GROUP2TEXT[self.group]