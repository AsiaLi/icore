# -*- coding: utf-8 -*-
from business.user.user import User

__author__ = 'Asia'

from rust.core import business

from db.account import models as account_models

class AccountFactory(business.Service):

    def create_user(self, param_obj):
        """
        创建用户
        """
        manager = self.user
        user_db_model = account_models.User.create(
            username = param_obj.username,
            email = param_obj.email,
            password = param_obj.password,

        )

        account_models.UserProfile.create(
            user_id = user_db_model.id,
            manager_id = manager.id,
            nick_name = param_obj.nick_name,
            remark = param_obj.remark,
        )

        return User(user_db_model.id)

    def update_user(self, param_obj):
        """
        编辑用户信息
        """
        user_id = param_obj.user_id
        account_models.User.update(
            email=param_obj.email,
        ).where(account_models.User.id==user_id).execute()

        account_models.UserProfile.update(
            nick_name = param_obj.nick_name,
            remark = param_obj.remark,
            phone = param_obj.phone,
            birthday = param_obj.birthday,

        ).where(account_models.User.id==user_id).execute()