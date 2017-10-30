# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core.decorator import param_required
from rust.core import api_resource

from api import ParamObject

class AUser(api_resource.ApiResource):
    """
    使用系统的用户
    """
    app = 'account'
    resource = 'user'

    @param_required(['user_id', 'username:str', 'phone:str', 'birthday:str', '?email:str',
                     '?nick_name:str', 'password', '?remark:str'])
    def put(args):
        param_obj = ParamObject({
            'username': args['username'],
            'nick_name': args.get('nick_name', args['username']),
            'password': args['password'],
            'phone': args['phone'],
            'birthday': args['birthday'],
            'email': args.get('email', ''),
            'remark': args.get('remark', ''),
        })

        manager = args['user']
        manager.account_factory.create_user(param_obj)
        return {}

    @param_required(['user_id', 'id', 'phone:str', 'birthday:str', 'email:str',
                     'nick_name:str', 'remark:str'])
    def post(args):
        param_obj = ParamObject({
            'user_id': args['id'],
            'nick_name': args.get('nick_name', args['username']),
            'phone': args['phone'],
            'birthday': args['birthday'],
            'email': args['email'],
            'remark': args['remark'],
        })

        manager = args['user']
        manager.account_factory.update_user(param_obj)
        return {}