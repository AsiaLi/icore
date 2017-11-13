# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core import business
from rust.core.decorator import cached_context_property

from db.member import models as member_models

class Member(business.Model):

    __slots__ = (
        'id',
        'name',
        'role',
    )

    def __init__(self, member_id):
        business.Model.__init__(self)
        self.id = member_id

    @cached_context_property
    def __member(self):
        return member_models.Member.select().where(
            member_models.Member.id == self.id).first()

    @cached_context_property
    def name(self):
        return self.__member.name

    def is_manager(self):
        from db.family import models as family_models
        return family_models.Family.select().where(
            family_models.Family.manager_id == self.id
        ).first()