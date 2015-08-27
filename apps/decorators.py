from functools import wraps
from flask import session, flash, redirect, url_for, abort

from apps.models import User


def current_user():
    user = None
    if 'user_id' in session:
        user_id = session['user_id']
        user = User.get(User.id == user_id)
    return user


def admin_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not current_user():
            flash('Anda harus masuk dahulu untuk melihat halaman ini', 'error')
            return redirect(url_for('login'))
        elif current_user():
            user = current_user()
            if user.level.name != 'admin':
                return abort(401)
            return func(*args, **kwargs)
    return decorator

def dosen_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not current_user():
            flash('Anda harus masuk dahulu untuk melihat halaman ini', 'error')
            return redirect(url_for('login'))
        elif current_user():
            user = current_user()
            if user.level.name != 'dosen':
                return abort(401)
            return func(*args, **kwargs)
    return decorator

def mhs_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not current_user():
            flash('Anda harus masuk dahulu untuk melihat halaman ini', 'error')
            return redirect(url_for('login'))
        elif current_user():
            user = current_user()
            if user.level.name != 'mahasiswa':
                return abort(401)
            return func(*args, **kwargs)
    return decorator
