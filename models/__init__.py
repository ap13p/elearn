from __future__ import absolute_import
from playhouse.flask_utils import FlaskDB

from app import app

db = FlaskDB(app)

from .auth import User, Level
from .others import MataKuliah, Tugas, Post, KumpulTugas

__all__ = ('db', 'User', 'Level',
           'MataKuliah', 'Tugas', 'Post',
           'KumpulTugas')
