#!/usr/bin/python3
"""
This script deletes out-of-date archives
Using the function do_clean function
"""
import os
from fabric.api import *

env.hosts = ["67.202.31.142", "34.204.76.17"]


def do_clean(number=0):
    """
    Function do_clean
    deletes out-of-date archives
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
