# -*- coding: utf-8 -*-
__author__ = 'Asia'

from rust.command.base_command import BaseCommand

from db.family import models as family_models

class Command(BaseCommand):
    help = "init family"
    args = ''

    def handle(self, **options):
        family_models.Family.create(
            name = 'aix`s family',
            manager_id = 1,
        )