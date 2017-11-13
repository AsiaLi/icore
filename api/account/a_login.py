# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

from db.member import models as member_models

class ALogin(api_resource.ApiResource):
    """
    登录
    """
    app = 'account'
    resource = 'login'

    @param_required(['name:str', 'password:str'])
    def put(args):
        db_models = member_models.Member.select().where(
            member_models.Member.name == args['name']
        )

        if db_models.count() == 0:
            return 500, u'用户名不存在'

        db_model = db_models.where(
            member_models.Member.password == args['password']
        ).first()

        if not db_model:
            return 500, u'密码错误'

        return {
            'member_id': db_model.id
        }
