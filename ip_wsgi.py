import os
import site
import sys


basedir = os.path.abspath(os.path.dirname(__file__))


if os.name == 'nt':
    site.addsitedir(os.path.join(basedir, '.venv/Lib/site-packages'))
else:
    site.addsitedir(os.path.join(basedir, '.venv/lib/python3.7/site-packages/'))
    site.addsitedir(os.path.join(basedir, '.venv/lib64/python3.7/site-packages/'))


sys.path.insert(0, basedir)


def application(environ, start_response):
    from app import app as _application
    return _application(environ, start_response)
