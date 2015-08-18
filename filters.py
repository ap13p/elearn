__author__ = 'Afief'

from dateutil import parser

def to_datetime(string, _format='%d-%m-%Y'):
    string = str(string)
    date = parser.parse(string)
    native = date.replace(tzinfo=None)
    return native.strftime(_format)
