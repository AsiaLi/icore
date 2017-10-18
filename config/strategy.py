# -*- coding: utf-8 -*-

STRATEGIES = {
    'order': [
        'business.order.strategy.ship_order_kuaidi_strategy',
        # 'business.order.strategy.update_order_status_strategy'
        # 'business.order.strategy.process_payment_order_strategy'
        'business.order.strategy.manage_order_statistics_strategy',
        'business.order.strategy.for_product_evaluation_strategy',
    ],
    'product': [
        'business.product.strategy.increase_sales_strategy'
    ],
    'imoney': [
        'business.payment.strategy.deposit_imoney_strategy'
    ],
    'member': [
        'business.member.strategy.manage_shopping_cart_item_strategy',
        'business.member.strategy.manage_member_consumption_info_strategy',
        'business.member.strategy.member_grade_strategy',
        'business.member.strategy.member_grade_pay_strategy',
    ]
}
