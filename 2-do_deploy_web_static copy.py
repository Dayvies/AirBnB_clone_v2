#!/usr/bin/python3
"""Fabric script that deploys and extracts files"""
import paramiko, os
paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG) 
paramiko.transport.disabled_keys = {'pubkeys':['rsa-sha2-512','rsa-sha2-256']} 
import os
from fabric.api import *
env.hosts = ['3.238.104.57']
env.user = 'ubuntu'
env.key_filename = 'key'


def do_deploy(archive_path):
        """deploys and extracts"""
        env.key_filename = ['key','~/.ssh/school']
        if not os.path.exists(archive_path):
               return False
        local('pwd')
        run('pwd')
        
