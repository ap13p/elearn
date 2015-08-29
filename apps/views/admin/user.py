from flask import render_template, request, url_for, redirect, g, flash
from flask_peewee.utils import object_list

from apps.forms.user import UserForm, get_level
from apps.models import Level, User, Profile
from apps.decorators import admin_required


@admin_required
def user_create():
    form = UserForm(request.form)
    form.action = url_for('admin:user:create')
    form.level.choices = get_level()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.password = form.password.data
        user.no_induk = form.no_induk.data
        level = Level.get(Level.id == form.level.data)
        jenkel = form.profile.jenis_kelamin.data
        nama = form.profile.nama.data
        profile = Profile.create(nama=nama, jenis_kelamin=jenkel)
        user.level = level
        user.profile = profile
        user.save()
        return redirect(url_for('admin:user:list'))
    if form.errors:
        print form.errors
    return render_template('admin/user/create.html', form=form)


@admin_required
def user_list():
    users = User.select()
    _level = request.args.get('level', None)
    if _level:
        users = users.join(Level).where(Level.name == _level)
    return object_list('admin/user/list.html', users, 'users', paginate_by=10)


@admin_required
def user_update(user_id):
    user = User.get(User.id == user_id)
    form = UserForm(request.form, obj=user)
    form.action = url_for('admin:user:update', user_id=user.id)
    form.level.choices = get_level()
    form.level.data = user.level.id
    form.profile.jenis_kelamin.data = user.profile.jenis_kelamin
    if form.validate_on_submit():
        form.populate_obj(user)
        user.level = Level.get(Level.id == form.level.data)
        user.profile.nama = form.profile.nama.data
        user.profile.save()
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
            user.delete_instance(True)
        return redirect(url_for('admin:user:list'))
    else:
        return redirect(url_for('login'))
