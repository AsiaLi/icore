# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.command.base_command import BaseCommand

from db.member import models as member_models

from new_member_config import NEW_MEMBER

class Command(BaseCommand):
    help = 'create member'
    args = ''

    def handle(self, **options):
        member_models.Member.create(
            name = NEW_MEMBER['name'],
            password = 'test',
            role = NEW_MEMBER['role']
        )
