#!/usr/bin/python
# coding=utf-8

import sys
import os
from kungfu.server.manager import execute

if __mian__ == '__main__':
    execute(sys.argv, os.path.abspath(os.path.dirname(__file__)))
