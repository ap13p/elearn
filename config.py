__author__ = 'Afief'

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(128))
DATABASE = os.getenv('OPENSHIFT_MYSQL_DB_URL', 'sqlite:///data.sqlite')
MEDIA_ROOT = os.getenv('OPENSHIFT_DATA_DIR', os.path.join(BASE_DIR, 'app_media_root'))

