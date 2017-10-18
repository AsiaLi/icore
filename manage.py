#!/usr/bin/env python

import sys
from rust.command import manage as command_manager

print sys.path

if __name__ == '__main__':
    command = sys.argv[1]
    command_manager.run_command(command)
