#!/usr/bin/python
import os

# virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtenv = os.path.join(os.getenv('OPENSHIFT_PYTHON_DIR', '.'), 'virtenv')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from apps import create_app
application = create_app()

#
# Below for testing only
#
if __name__ == '__main__':
    if os.getenv('LOCAL', False):
        application.run()
    else:
        from wsgiref.simple_server import make_server
        httpd = make_server('localhost', 8051, application)
        # Wait for a single request, serve it and quit.
        httpd.serve_forever()
