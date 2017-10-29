# -*- coding: utf-8 -*-

import os
import json

from rust.command.base_command import BaseCommand
from . import syncdb


class Command(BaseCommand):
	help = "rebuild database for service"
	args = ''
	
	def handle(self, **options):
		pass