"""Fabric script that deploys and extracts files"""
import os
import fabric
from fabric.api import *
from datetime import datetime
env.hosts = ['3.238.104.57', '44.200.43.53']
env.user = 'ubuntu'
env.key_filename = 'key'


def do_deploy(archive_path):
    """deploys and extracts"""
    pth = archive_path.split('/')[1]
    file = pth.split('.')[0]
    if not os.path.exists(archive_path):
        return False
    if put(archive_path, "/tmp/{}".format(pth)).failed:
        return False
    if sudo("mkdir -p /data/web_static/releases/{}/".format(file)).failed:
        return False
    if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(pth, file)).failed:
        return False
    if sudo("rm /tmp/{}".format(pth)).failed:
        return False
    if sudo("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(file, file)).failed:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/web_static"
            .format(file)).failed:
        return False
    if sudo("rm -rf /data/web_static/current").failed:
        return False
    if sudo("ln -sf /data/web_static/releases/{}/ /data/web_static/current"
            .format(file)).failed:
        return False
    print("New version deployed!")
    return True


@fabric.decorators.hosts("localhost")
@runs_once
def do_pack():
    """Fabric script that compresses a file"""
    now = datetime.now()
    if not os.path.exists('versions'):
        os.makedirs('versions')

    file = "versions/web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)
    print("Packing web_static to {}".format(file))
    local('tar -cvzf {} web_static'.format(file))
    try:
        file_size = os.path.getsize(file)
    except Exception:
        return None
    print("web_static packed: {} -> {}Bytes".format(file, file_size))
    return file


def deploy():
    """fetch then deploy"""
    path = do_pack()
    if not os.path.exists(path):
        return False
    result = do_deploy(path)
    return result
