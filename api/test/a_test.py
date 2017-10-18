# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.core import api_resource

class ATest(api_resource.ApiResource):

    app = 'test'
    resource = 'test'

    def get(args):
        return {
            'test': 'yeah'
        }
