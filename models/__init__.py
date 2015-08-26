from __future__ import absolute_import
from playhouse.flask_utils import FlaskDB

from app import app

db = FlaskDB(app)

from .auth import User, Level, Profile
from .others import MataKuliah, Tugas, Post, KumpulTugas, Phile

__all__ = ('db', 'User', 'Level', 'Profile',
           'MataKuliah', 'Tugas', 'Post',
           'KumpulTugas', 'Phile')
