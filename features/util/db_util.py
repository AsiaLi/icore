# -*- coding: utf-8 -*-
from db.account import models as account_models
from db.mall import models as mall_models
from db.member import models as member_models
from db.weixin import models as weixin_user_models
from db.group import models as group_models

from business.corporation.corporation_factory import CorporationFactory

def get_product(corp_name, product_name):
    corp = CorporationFactory.get_corporation_by_name(corp_name)

    db_product = mall_models.Product.select().dj_where(name=product_name).get()
    if mall_models.ProductPool.select().dj_where(woid=corp.id, product_id=db_product.id).count() > 0:
        return db_product
    else:
        raise RuntimeError(u"NO PRODUCT FOR <%s, %s>" % (corp_name, product_name))

def get_latest_order(member=None):
    """
    获得最新创建的订单
    """
    options = {
        'type': mall_models.ORDER_TYPE_ORDER
    }
    if member:
        options['member_id'] = member.id

    return mall_models.Order.select().dj_where(**options).order_by(-mall_models.Order.id).first()


def get_latest_delivery_item(member=None):
    """
    获得最新创建的订单
    """
    options = {
        'type': mall_models.ORDER_TYPE_INVOICE
    }
    if member:
        options['member_id'] = member.id

    return mall_models.Order.select().dj_where(**options).order_by(-mall_models.Order.id).first()



def get_latest_delivery_item_for_corp(corp):
    """
    获得corp的最新出货单
    """
    options = {
        'type': mall_models.ORDER_TYPE_INVOICE
    }
    options['supplier_corp_id'] = corp.id

    return mall_models.Order.select().dj_where(**options).order_by(-mall_models.Order.id).first()


def get_orders_for_bid_group(member, bid_group):
    """
    获取以bid_group为前缀的订单model集合
    """
    options = {
        'member_id': member.id
    }

    db_models = []
    index = 0
    while True:
        bid = '%s%s' % (bid_group, index)
        options['bid'] = bid
        if mall_models.Order.select().dj_where(**options).count() == 0:
            break
        else:
            db_model = mall_models.Order.select().dj_where(**options).get()
            db_models.append({
                'index': index,
                'db_model': db_model
            })

        index += 1

    return db_models


def get_default_ship_info_for_member(member):
    """
    获取member的默认收货地址
    """
    db_model = member_models.ShipInfo.select().dj_where(webapp_user_id=member.id, is_default=True).get()
    return db_model