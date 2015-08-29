from flask import render_template, g, flash, redirect, url_for, request
from flask_peewee.utils import object_list
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from peewee import fn, JOIN

from apps.forms.others import TugasForm
from apps.models import KumpulTugas, Tugas, MataKuliah, TugasFile, Phile
from apps.decorators import dosen_required, current_user
from apps.views import generate_path


@dosen_required
def home():
    return redirect(url_for('dosen:tugas:list'))


@dosen_required
def tugas_list():
    tugass = (
    Tugas.select(Tugas, fn.Count(KumpulTugas.id).alias('k_tugas_count'))
    .join(KumpulTugas, JOIN.LEFT_OUTER, on=(KumpulTugas.tugas == Tugas.id))
    .join(MataKuliah, on=(Tugas.mata_kuliah == MataKuliah.id))
    .group_by(Tugas)
    .where(MataKuliah.dosen == current_user()))

    return object_list('dosen/tugas/list.html', tugass, var_name='tugass',
                       paginate_by=10)


@dosen_required
def tugas_delete(tugas_id):
    if g.user and g.user.level.name == 'dosen':
        tugas = None
        try:
            tugas = Tugas.get(Tugas.id == tugas_id)
        except Tugas.DoesNotExist:
            flash('Tidak bisa menghapus tugas', 'error')
        if tugas:
            tugas.delete_instance(True)
            flash('Sukses menghapus tugas')
        return redirect(url_for('dosen:tugas:list'))
    return render_template('dosen/tugas/list.html')


@dosen_required
def tugas_update(tugas_id):
    tugas = Tugas.get(Tugas.id == tugas_id)
    user = g.user
    form = TugasForm(request.form, obj=tugas)
    form.action = url_for('dosen:tugas:update', tugas_id=tugas_id)
    matkul = MataKuliah.get(MataKuliah.dosen == user)
    if form.validate_on_submit():
        form.populate_obj(tugas)
        tugas.mata_kuliah = matkul
        tugas.save()
        flash('Sukses memperbarui tugas')
        return redirect(url_for('dosen:tugas:list'))
    return render_template('dosen/tugas/update.html', form=form)


@dosen_required
def tugas_create():
    form = TugasForm(request.form)
    if form.validate_on_submit():
        tugas = Tugas()
        form.populate_obj(tugas)
        user = g.user
        matkul = MataKuliah.get(MataKuliah.dosen == user)
        tugas.mata_kuliah = matkul
        tugas.save()

        file_list = request.files.getlist('file_pendukung')
        for f in file_list:
            if isinstance(f, FileStorage):
                import os
                save_to = os.path.join(generate_path(),
                                       secure_filename(user.email))
                if not os.path.exists(save_to):
                    os.makedirs(save_to)
                save_to = os.path.join(save_to, secure_filename(f.filename))
                f.save(save_to)
                p = Phile.create(
                    filename=f.filename,
                    filepath=save_to,
                    filetype=f.mimetype
                )
                TugasFile.create(tugas=tugas, phile=p)
        flash('Sukses membuat tugas')
        return redirect(url_for('dosen:tugas:list'))
    return render_template('dosen/tugas/create.html', form=form)


@dosen_required
def tugas_detail(tugas_id):
    tugas = (Tugas.select(Tugas, KumpulTugas)
             .join(KumpulTugas, JOIN.LEFT_OUTER,
                   on=(KumpulTugas.tugas == Tugas.id))
             .where(Tugas.id == tugas_id)).get()
    return render_template('dosen/tugas/detail.html', tugas=tugas)
