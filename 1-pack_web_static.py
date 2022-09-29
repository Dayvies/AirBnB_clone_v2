#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the web_static folder"""
from fabric.api import local, run
from datetime import datetime
import os


def do_pack():
    """Fabric script that compresses a file"""
    now = datetime.now()
    if not os.path.exists('versions'):
        os.makedirs('versions')

    file = "versions/web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    print ("Packing web_static to {}".format(file))
    local('tar -cvzf {} web_static'.format(file))
    file_size = os.path.getsize(file)
    print ("web_static packed: {} -> {}Bytes".format(file,file_size))
