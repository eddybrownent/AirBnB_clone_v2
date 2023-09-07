#!/usr/bin/python3
"""
This fabric script desploys an archive to web servers
"""
from fabric.api import env, run, put
import os


env.hosts = ['54.197.21.126', '54.236.56.228']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    distributes an archive to webservers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        """
        Upload archive to /tmp/ directory in web server
        """
        put(archive_path, '/tmp/')

        """
        extracting the archive to /data/web_static/releases/ directory
        """
        archive_name = os.path.basename(archive_path)
        folder = archive_name.split('.')[0]
        extract_path = "/data/web_static/releases/{}".format(folder)

        run("mkdir -p {}".format(extract_path))
        run("tar -xzf /tmp/{} -C {}".format(
            archive_name, extract_path))

        """
        Deleting the archive from the server
        """
        run("rm /tmp/{}".format(archive_name))

        """
        Move extracts to new folder
        """
        run("mv {}/web_static/* {}/".format(extract_path, extract_path))

        """
        Remove extracted folder from remote server
        """
        run("rm -rf {}/web_static".format(extract_path))

        """
        Removing the current symbolic link
        """
        c_link = "/data/web_static/current"
        run("rm -rf {}".format(c_link))

        """
        Creating new symbolic link pointing to the new page
        """
        run("ln -s {} {}".format(extract_path, c_link))

        print("New version deployed!")

        return True
    except Exception:
        return False
