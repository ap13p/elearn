import os

from flask import render_template, request, url_for, current_app, \
    redirect, g
from peewee import JOIN
from werkzeug.datastructures import FileStorage

from werkzeug.utils import secure_filename

from apps.forms.others import KumpulkanTugasForm
from apps.models import User, Tugas, KumpulTugas, MataKuliah, Post, Level, \
    Phile, Profile, TugasFile
from apps.decorators import mhs_required, current_user


def generate_path(user_id, tugas_id):
    app = current_app
    user = current_user()
    path = os.path.join(app.config['MEDIA_ROOT'], 'uploads', user_id, 'tugas',
                        tugas_id)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


@mhs_required
def home():
    dosens = (User.select(User, MataKuliah)
              .join(MataKuliah)
              .join(Level, JOIN.LEFT_OUTER, on=(User.level == Level.id))
              .join(Tugas, JOIN.LEFT_OUTER,
                    on=(Tugas.mata_kuliah == MataKuliah.id))
              .join(Profile, on=(User.profile == Profile.id))
              .group_by(User)
              .where(Level.name == 'dosen')
              .order_by(Profile.nama.asc()))
    dosen_id = request.args.get('dosen_id', None)
    if dosen_id:
        dosen = dosens.filter(User.id == dosen_id).get()
    else:
        dosen = dosens.first()
        dosen_id = dosen.id
    posts = Post.select().order_by(Post.id.desc())
    user = g.user
    return render_template('mhs/home.html', dosen=dosen, dosens=dosens,
                           posts=posts, dosen_id=dosen_id)


@mhs_required
def tugas_detail(tugas_id):
    user = current_user()
    dosens = (User
              .select(User, MataKuliah.judul, Profile.nama)
              .join(MataKuliah, on=(MataKuliah.dosen == User.id))
              .join(Level, JOIN.LEFT_OUTER, on=(User.level == Level.id))
              .join(Profile, on=(User.profile == Profile.id))
              .group_by(User)
              .where(Level.name == 'dosen')
              .order_by(Profile.nama.asc()))
    tugas = Tugas.get(Tugas.id == tugas_id)
    dosen_id = tugas.mata_kuliah.dosen.id
    file_list = TugasFile.select().where(TugasFile.tugas == tugas)
    try:
        sudah_mengumpulkan = KumpulTugas.get(KumpulTugas.tugas == tugas,
                                             KumpulTugas.mahasiswa == user)
    except KumpulTugas.DoesNotExist:
        sudah_mengumpulkan = False
    form = KumpulkanTugasForm(request.form)
    form.action = url_for('mhs:tugas:kumpulkan', tugas_id=tugas.id)
    return render_template('mhs/detail.html', tugas=tugas, dosens=dosens,
                           form=form,
                           sudah_mengumpulkan=sudah_mengumpulkan,
                           dosen_id=dosen_id,
                           file_list=file_list)


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
