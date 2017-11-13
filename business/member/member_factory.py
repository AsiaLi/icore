# -*- coding: utf-8 -*-
from business.member.member import Member

__author__ = 'Asia'

from rust.core import business

from db.member import models as member_models

class MemberFactory(business.Service):

    def create_member(self, param_obj):
        """
        创建用户
        """
        member_db_model = member_models.Member.create(
            name = param_obj.username,
            role = param_obj.role,
            phone = param_obj.phone,
            email = param_obj.email,
            password = param_obj.password,

        )

        return Member(member_db_model.id)

    def update_member(self, param_obj):
        """
        编辑用户信息
        """
        member_id = param_obj.member_id
        member_models.Member.update(
            phone = param_obj.phone,
            email = param_obj.email,
        ).where(member_models.Member.id==member_id).execute()