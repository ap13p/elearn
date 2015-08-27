__author__ = 'Afief'

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY', '12345')
DATABASE = os.getenv('OPENSHIFT_MYSQL_DB_URL', 'mysql://apiep:qwe123@localhost/cc_ellearn')
MEDIA_ROOT = os.getenv('OPENSHIFT_DATA_DIR', os.path.join(BASE_DIR, 'app_media_root'))
DEBUG_TB_INTERCEPT_REDIRECTS = False
