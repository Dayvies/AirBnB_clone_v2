#!/usr/bin/python3
"""Fabric script that deploys and extracts files"""
import os
from fabric.api import *
env.hosts = ['3.238.104.57', '44.200.43.53']
env.user = 'ubuntu'
env.key_filename = 'key'


def do_deploy(archive_path):
    """deploys and extracts"""
    pth = archive_path.split('/')[1]
    file = pth.split('.')[0]
    if not os.path.exists(archive_path):
        print(pth)
        print(file)
        return False
    if put(archive_path, "/tmp/{}".format(pth)).failed:
        return False
    if sudo("mkdir -p /data/web_static/releases/{}/".format(file)).failed:
        return False
    if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(pth, file)).failed:
        return False
    if sudo("rm /tmp/{}".format(pth)).failed:
        return False
    if sudo("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(file, file)).failed:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/web_static".format(file)).failed:
        return False
    if sudo("rm -rf /data/web_static/current").failed:
        return False
    if sudo("ln -sf /data/web_static/releases/{}/ /data/web_static/current".format(file)).failed:
        return False
    print("New version deployed")
    return True
