from flask import render_template, g, flash, redirect, url_for, request
from flask_peewee.utils import object_list
from forms.others import TugasForm
from models import KumpulTugas, Tugas, MataKuliah, User
from decorators import dosen_required


@dosen_required
def home():
    return render_template('dosen/home.html')

@dosen_required
def tugas_list():
    tugass = Tugas.select()
    return object_list('dosen/tugas/list.html', tugass, var_name='tugass', paginate_by=10)

@dosen_required
def tugas_delete(tugas_id):
    if g.user and g.user.level.name == 'dosen':
        tugas = None
        try:
            tugas = Tugas.get(Tugas.id == tugas_id)
        except Tugas.DoesNotExist:
            flash('Tidak bisa menghapus tugas', 'error')
        if tugas:
            tugas.delete_instance()
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
        flash('Sukses membuat tugas')
        return redirect(url_for('dosen:tugas:list'))
    return render_template('dosen/tugas/create.html', form=form)

@dosen_required
def tugas_detail(tugas_id):
    tugas = Tugas.get(Tugas.id == tugas_id)
    mhs_yg_mengumpulkan = KumpulTugas.select().where(KumpulTugas.tugas == tugas)
    return render_template('dosen/tugas/detail.html', tugas=tugas, mhs_yg_mengumpulkan=mhs_yg_mengumpulkan)
