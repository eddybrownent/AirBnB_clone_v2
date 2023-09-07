#!/usr/bin/python3
"""
This fabric script desploys an archive to web servers
"""
from fabric.api import env, run, put
import os


env.hosts = ['54.197.21.126', '54.236.56.228']


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
        extract_file = "/data/web_static/releases/{}".format(
                archive_name.split('.')[0])

        run("mkdir -p {}".format(extract_file))
        run("tar -xzf /tmp/{} -C {}".format(
            archive_name, extract_file))

        """
        Deleting the archive from the server
        """
        run("rm /tmp/{}".format(archive_name))

        """
        Removin the current symbolic link
        """
        c_link = "/data/web_static/current"
        run("rm -rf {}".format(c_link))

        """
        Creating new symbolic link pointing to the new page
        """
        run("ln -s {} {}".format(extract_file, c_link))

        print("New version deployed!")

        return True
    except Exception:
        return False
