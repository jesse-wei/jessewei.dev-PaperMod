"""Source: https://stackoverflow.com/a/24176022

Change cwd within Python like so

os.chdir('/home')

with cd('/tmp'):
    # ...

# Directory is now back to '/home'"""

from contextlib import contextmanager
import os

@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)
