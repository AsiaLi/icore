# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core import business
from rust.core.decorator import cached_context_property

from db.account import models as account_models

class User(business.Model):

    __slots__ = (
        'id',
        'username',
        'nick_name',
    )

    def __init__(self, user_id):
        business.Model.__init__(self)
        self.id = user_id

    @cached_context_property
    def __user(self):
        return account_models.User.select().where(account_models.User.id==self.id).first()

    @cached_context_property
    def __profile(self):
        return account_models.UserProfile.select().where(account_models.UserProfile.user_id == self.id).first()

    @cached_context_property
    def username(self):
        return self.__user.username

    @cached_context_property
    def nick_name(self):
        return self.__profile.nick_name


    @property
    def account_factory(self):
        from business.user.account_factory import AccountFactory
        return AccountFactory(self)