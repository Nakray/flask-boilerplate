import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    db_user = os.environ.get('DB_USERNAME')
    db_pass = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_name = os.environ.get('DB_NAME')

    SQLALCHEMY_DATABASE_URI = "postgresql://%s:%s@%s:%s/%s" % (db_user, db_pass, db_host, db_port, db_name)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
