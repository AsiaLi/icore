# -*- coding: utf-8 -*-

from eaglet.core import watchdog

from business.corporation.corporation import Corporation
from business.corporation.corporation_factory import CorporationFactory

class AccountMiddleware(object):
	def process_request(sel, req, resp):
		if '/user/access_token' in req.path or '/console' in req.path:
			watchdog.info("skipped in WebAppAccountMiddleware. req.path: {}".format(req.path))
			return

		if '/webapp.' in req.path:
			watchdog.info("skipped in WebAppAccountMiddleware. req.path: {}".format(req.path))
			return

		if '/static/' in req.path:
			return

		if '/pay/dlb_callback' in req.path:
			return
		
		if '/express/callback' in req.path:
			return

		if not req.context.get('corp'):
			corp_id = req.params.get('corp_id')
			if corp_id:
				req.context['corp'] = Corporation(int(corp_id))
				CorporationFactory.set(req.context['corp'])
