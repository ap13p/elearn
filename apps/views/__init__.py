import os
from datetime import datetime

from flask import render_template, request, flash, session, url_for, redirect, \
    send_file, current_app, jsonify, g, abort
from flask_peewee.utils import object_list, get_object_or_404
from werkzeug.utils import secure_filename

from apps.forms import LoginForm
from apps.forms.user import UpdateInfoForm, ChangePasswordForm
from apps.models import Post, User, Profile, Phile


def generate_path():
    app = current_app
    now = datetime.now()
    year = str(now.strftime('%Y'))
    month = str(now.strftime('%m'))
    day = str(now.strftime('%d'))
    path = os.path.join(app.config['MEDIA_ROOT'], 'uploads', year, month, day)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def home():
    posts = Post.select().where(Post.publik == True)
    return object_list('home.html', posts, var_name='posts')


def blog_detail(post_id):
    post = get_object_or_404(Post, Post.id == post_id)
    return render_template('detail.html', post=post)


def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            user = User.get(User.email == email)
            if user and user.check_password(password):
                session['user_id'] = user.id
                session.permanent = True
                return redirect(url_for('home'))
            else:
                flash('Email atau password salah', 'error')
                return render_template('login.html', form=form)
        except User.DoesNotExist:
            flash('Email atau password salah', 'error')
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


def logout():
    if 'user_id' in session:
        session['user_id'] = None
        del session['user_id']
    return redirect(url_for('home'))


def sendfile(file_id, download=False):
    phile = Phile.get(Phile.id == file_id)
    filepath = phile.filepath
    download = bool(request.args.get('download', False))
    return send_file(filepath, as_attachment=download)


def upload():
    phile = request.files.get('upload', None)
    if phile:
        path = generate_path()
        filepath = os.path.join(path, secure_filename(phile.filename))
        phile.save(filepath)
        f = Phile()
        f.filename = phile.filename
        f.filetype = phile.mimetype
        f.filepath = filepath
        f.save()
        return jsonify({
            'uploaded': 1,
            'filename': f.filename,
            'url': url_for('sendfile', file_id=f.id)
        })
    return jsonify({
        'uploaded': 0,
        'error': {
            'message': 'File cannot be uploaded'
        }
    })


def get_user_media_path(user):
    import os
    from flask import current_app as app
    path = os.path.join(app.config['MEDIA_ROOT'], secure_filename(user.email))
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def update_info(user_id):
    if not g.user.id == user_id:
        return abort(401)
    user = User.select().join(Profile).where(User.id == user_id).get()
    form = UpdateInfoForm(request.form, obj=user)
    form.action = url_for('update-info', user_id=user_id)
    if form.validate_on_submit():
        user.profile.nama = form.profile.nama.data
        user.profile.no_telpon = form.profile.no_telpon.data
        user.profile.tanggal_lahir = form.profile.tanggal_lahir.data
        user.profile.alamat = form.profile.alamat.data
        path = get_user_media_path(user)
        phile = request.files['profile-image']
        if phile:
            path = os.path.join(path, secure_filename(phile.filename))
            phile.save(path)
            user.profile.image = url_for('media', filepath=path)
        user.profile.save()
        user.save()
        return redirect(url_for('mhs:home'))
    return render_template('update_info.html', form=form, user=user)


def media(filepath):
    return send_file(filepath)


def change_password(user_id):
    user = get_object_or_404(User, User.id == user_id)
    form = ChangePasswordForm(request.form)
    form.action = url_for('change-password', user_id=user_id)
    if user.level.name == 'admin':
        next_url = url_for('admin:home')
    elif user.level.name == 'dosen':
        next_url = url_for('dosen:home')
    elif user.level.name == 'mahasiswa':
        next_url = url_for('mhs:home')
    else:
        next_url = url_for('home')

    if form.validate_on_submit():
        if not user.check_password(form.password_lama.data):
            flash('Salah password lama', 'error')
        else:
            user.password = form.password_baru.data
            user.save()
            return redirect(next_url)
    return render_template('change_password.html', form=form, user=user,
                           next_url=next_url)
