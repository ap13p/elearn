import os
from flask import render_template, g, flash, request, url_for, current_app, redirect
from forms.others import KumpulkanTugasForm
from models import User, Tugas, KumpulTugas, MataKuliah, Post, Level, Phile, Profile
from decorators import mhs_required, current_user
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename


def generate_path(user_id, tugas_id):
    app = current_app
    user = current_user()
    path = os.path.join(app.config['MEDIA_ROOT'], 'uploads', user_id, 'tugas', tugas_id)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


@mhs_required
def home():
    lvl_dosen = Level.select().where(Level.name == 'dosen')
    dosens = User.select().where(User.level == lvl_dosen)
    dosen_id = request.args.get('dosen_id', None)
    if dosen_id:
        dosen = dosens.filter(User.id == dosen_id).get()
    else:
        dosen = dosens.first()
    matkul = MataKuliah.get(MataKuliah.dosen == dosen)
    tugass = Tugas.select().where(Tugas.mata_kuliah == matkul)
    posts = Post.select().order_by(Post.id.desc())
    return render_template('mhs/home.html', dosen=dosen, dosens=dosens, tugass=tugass, posts=posts)


@mhs_required
def tugas_detail(tugas_id):
    lvl_dosen = Level.select().where(Level.name == 'dosen')
    dosens = User.select().join(Profile).where(User.level == lvl_dosen)
    tugas = Tugas.get(Tugas.id == tugas_id)
    user = current_user()
    try:
        sudah_mengumpulkan = KumpulTugas.get(KumpulTugas.tugas == tugas, KumpulTugas.mahasiswa == user)
    except KumpulTugas.DoesNotExist:
        sudah_mengumpulkan = False
    form = KumpulkanTugasForm(request.form)
    form.action = url_for('mhs:tugas:kumpulkan', tugas_id=tugas.id)
    return render_template('mhs/detail.html', tugas=tugas, dosens=dosens, form=form,
                           sudah_mengumpulkan=sudah_mengumpulkan)


@mhs_required
def tugas_kumpulkan(tugas_id):
    tugas = Tugas.get(Tugas.id == tugas_id)
    user = current_user()
    kumpul_tugas = KumpulTugas()
    kumpul_tugas.mahasiswa = user
    kumpul_tugas.tugas = tugas
    phile = request.files['phile']
    if isinstance(phile, FileStorage):
        path = generate_path(str(user.id), str(tugas.id))
        path = os.path.join(path, secure_filename(phile.filename))
        phile.save(path)
        f = Phile()
        f.filename = phile.filename
        f.filetype = phile.mimetype
        f.filepath = path
        f.save()
        kumpul_tugas.phile = f
    kumpul_tugas.save()
    return redirect(url_for('mhs:tugas:detail', tugas_id=tugas.id))
