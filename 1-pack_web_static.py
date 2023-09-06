#!/usr/bin/python3
"""
THis Fabric script generates a .tgz archive from the contents of a file
"""
from fabric.api import local
from fatetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    try:
        # Create the "versions" directory if it doesn't exist
        local("mkdir -p versions")

        # seting the time 
        time = datetime.now().strftime("%Y%m%d%H%M%S")

        # creating the name
        archive_name = "web_static_{}.tgz".format(time)

        # navigating to web_static dir using local context
        with lcd(web_static):
            # creating the .tgz
            local("tar -cvzf ../versions/{} .",.format(archive_name))

        # Check if archive was created successfully and return the path
        archive_path = "versions/{}".format(archive_name)
        return archive_path
    except Exception as e:
        return None
