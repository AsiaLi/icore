# -*- coding: utf-8 -*-

from rust.core.decorator import param_required
from rust.core import business

COUNT_PER_PAGE = 20

class PageInfo(business.Model):
    """
    分页
    """
    __slots__ = (
        'cur_page',
        'count_per_page'
    )
    
    def __init__(self, cur_page, count_per_page):
        self.cur_page = cur_page
        self.count_per_page = count_per_page

    @staticmethod
    @param_required(['cur_page'])
    def create(args):
        return PageInfo(args['cur_page'], args.get('count_per_page', COUNT_PER_PAGE))

    @staticmethod
    def get_max_page():
        return PageInfo(1, 9999999)