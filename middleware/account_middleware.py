# -*- coding: utf-8 -*-

from rust.core.base_middleware import BaseMiddleware

from business.member.member import Member


class AccountMiddleware(BaseMiddleware):
	def process_request(sel, req, resp):
		if '/webapp' in req.path:
			print 'skip webapp request'
			return

		if '/static/' in req.path:
			return

		member_id = req.params.get('member_id')
		if member_id:
			member = Member(member_id)
			req.context['member'] = member

	def process_response(self, request, response, resource):
		pass