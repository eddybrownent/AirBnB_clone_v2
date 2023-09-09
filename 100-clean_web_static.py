#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import env, lcd, cd, run, local

# defining the hosts
env.hosts = ["54.236.56.228", "54.197.21.126"]


def do_clean(number=0):
    """
    deletes out-of-date archives
    Args:
    number (int): The number of archives to keep
    """
    # set numbert to 1 if its 0 to keep most recent
    number = 1 if int(number) == 0 else int(number)

    # list archives in local dir and sort
    archives = sorted(os.listdir('versions'))

    # removing oldest number from the dir
    for i in range(number):
        archives.pop()

    # deleting out-of-date archives in the dir
    with lcd('versions'):
        for archive in archives:
            local("rm ./{}".format(archive))

    # listing archives in the hosts dir
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()

    # filtering for archives with web_static in names
    archives = [a for a in archives if "web_static_" in a]

    # removing the oldest number:
    for i in range(number):
        archives.pop()

    # deleting out-of-date archives in hosts
    for archive in archives:
        run("rm -rf ./{}".format(archive))
