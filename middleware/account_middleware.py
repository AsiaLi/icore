# -*- coding: utf-8 -*-

from rust.core.base_middleware import BaseMiddleware

class AccountMiddleware(BaseMiddleware):
	def process_request(sel, req, resp):
		if '/webapp.' in req.path:
			print 'skip webapp request'
			return

		if '/static/' in req.path:
			return
	def process_response(self, request, response, resource):
		pass