#!/usr/bin/python3
"""Fabric script that deploys and extracts files"""
import os
from fabric.api import *
env.hosts = ['3.238.104.57', '44.200.43.53']
env.user = 'ubuntu'
env.key_filename = 'key'


def do_clean(number=0):
    """deletes old files"""

    if number == '0':
        number = '1'
    number = int(number) + 1
    local("(cd ./versions && ls -t | tail -n +{}| xargs rm -rf)".format(number))
    run("(cd /data/web_static/releases && sudo ls -t .| tail -n +{}|xargs sudo rm -rf)".format(number))
