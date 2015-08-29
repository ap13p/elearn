from flask import request, url_for, redirect, flash, render_template, g
from flask_peewee.utils import object_list

from apps.forms.others import MataKuliahForm, get_dosen
from apps.models import MataKuliah, User
from apps.decorators import admin_required


@admin_required
def matkul_list():
    matkuls = MataKuliah.select().order_by(MataKuliah.kode.desc())
    return object_list('admin/matkul/list.html', matkuls, var_name='matkuls',
                       paginate_by=10)


@admin_required
def matkul_create():
    form = MataKuliahForm(request.form)
    form.dosen.choices = get_dosen()
    form.action = url_for('admin:matkul:create')
    if form.validate_on_submit():
        matkul = MataKuliah()
        form.populate_obj(matkul)
        matkul.dosen = User.get(User.id == form.dosen.data)
        matkul.save()
        flash('Sukses menambah mata kuliah')
        return redirect(url_for('admin:matkul:list'))
    return render_template('admin/matkul/create.html', form=form)


@admin_required
def matkul_update(matkul_id):
    matkul = MataKuliah.get(MataKuliah.id == matkul_id)
    form = MataKuliahForm(request.form, obj=matkul)
    form.dosen.choices = get_dosen()
    form.action = url_for('admin:matkul:update', matkul_id=matkul.id)
    if form.validate_on_submit():
        form.populate_obj(matkul)
        matkul.dosen = User.get(User.id == form.dosen.data)
        matkul.save()
        flash('Sukses memperbarui mata kuliah')
        return redirect(url_for('admin:matkul:list'))
    return render_template('admin/matkul/update.html', form=form)


@admin_required
def matkul_delete(matkul_id):
    if g.user and g.user.level.name == 'admin':
        matkul = None
        try:
            matkul = MataKuliah.get(MataKuliah.id == matkul_id)
        except MataKuliah.DoesNotExist:
            flash('Tidak bisa menghapus mata kuliah')
        if matkul:
            matkul.delete_instance()
            flash('Sukses menghapus mata kuliah')
        return redirect(url_for('admin:matkul:list'))
    return redirect(url_for('login'))
