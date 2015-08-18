from forms.user import UserForm, get_level, LevelForm
from models import Level, User
from flask import render_template, request, url_for, redirect, g, flash
from flask_peewee.utils import object_list
from decorators import admin_required


@admin_required
def user_create():
    form = UserForm(request.form)
    form.action = url_for('admin:user:create')
    form.level.choices = get_level()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        level = Level.get(Level.id == form.level.data)
        user.level = level
        user.save()
        return redirect(url_for('admin:user:list'))
    return render_template('admin/user/create.html', form=form)

@admin_required
def user_list():
    users = User.select().join(Level)
    return object_list('admin/user/list.html', users, 'users', paginate_by=10)

@admin_required
def user_update(user_id):
    user = User.get(User.id == user_id)
    form = UserForm(request.form, obj=user)
    form.action = url_for('admin:user:update', user_id=user.id)
    form.level.choices = get_level()
    if form.validate_on_submit():
        form.populate_obj(user)
        user.level = Level.get(Level.id == form.level.data)
        user.save()
        return redirect(url_for('admin:user:list'))
    return render_template('admin/user/update.html', form=form, user=user)

@admin_required
def user_delete(user_id):
    if g.user and g.user.level.name == 'admin':
        try:
            user = User.get(User.id == user_id)
        except User.DoesNotExist:
            flash('Tidak bisa menghapus user', 'error')
            return redirect(url_for('admin:user:list'))
        if user:
            user.delete_instance()
        return redirect(url_for('admin:user:list'))
    else:
        return redirect(url_for('login'))
