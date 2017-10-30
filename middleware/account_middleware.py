# -*- coding: utf-8 -*-

from rust.core.base_middleware import BaseMiddleware

from business.user.user import User


class AccountMiddleware(BaseMiddleware):
	def process_request(sel, req, resp):
		if '/webapp' in req.path:
			print 'skip webapp request'
			return

		if '/static/' in req.path:
			return

		if not req.context.get('user'):
			user_id = req.params.get('user_id')
			if user_id:
				user = User(user_id)
				req.context['user'] = user


	def process_response(self, request, response, resource):
		pass