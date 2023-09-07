#!/usr/bin/python3
"""
script that creates and distributes an archive to your web servers
"""

from fabric.api import env, run, put, local
from os.path import exists
from datetime import datetime
import os

env.hosts = ['54.197.21.126', '54.236.56.228']
env.user = 'ubuntu'
env.key_filename = ['/root/.ssh/my_ssh_key']


def do_pack():
    """
    Compresses web_static folder to a .tgz archive
    """
    time_format = "%Y%m%d%H%M%S"
    now = datetime.utcnow().strftime(time_format)
    file_path = "versions/web_static_{}.tgz".format(now)

    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(file_path))
    if result.failed:
        return None
    return file_path


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_name = os.path.basename(archive_path).split('.')[0]
        remote_path = "/data/web_static/releases/{}/".format(archive_name)

        run("mkdir -p {}".format(remote_path))
        run("tar -xzf /tmp/{}.tgz -C {}".format(
            archive_name, remote_path))
        run("rm /tmp/{}.tgz".format(archive_name))
        run("mv {}/web_static/* {}".format(remote_path, remote_path))
        run("rm -rf {}/web_static".format(remote_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(remote_path))

        return True
    except Exception:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
