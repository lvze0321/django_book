#!/usr/bin/env python
#coding=utf-8
import os
import sys

if __name__ == "__main__":
    #设置配置文件，在使用manage时系统知道遵循哪个settings的配置
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booksite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
