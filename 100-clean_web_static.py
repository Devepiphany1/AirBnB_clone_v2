#!/usr/bin/python3
"""
this script delete out-of-date archives fab -f 100-clean_web_static.py do_clean:number=2 -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['100.27.12.148', '54.166.105.15']


def do_clean(number=0):
    """this delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, while
    number is 2, keeps the most and second-most recent archives,
    etc.
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
