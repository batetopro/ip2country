import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB = dict(
        HOST=os.environ.get('DATABASE_HOST') or "127.0.0.1",
        USER=os.environ.get('DATABASE_USER') or "root",
        PASSWORD=os.environ.get('DATABASE_PASSWORD') or "",
        BASE=os.environ.get('DATABASE_BASE') or "ip2country",
    )




