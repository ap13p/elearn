import os
from datetime import datetime
from flask import render_template, request, flash, session, url_for, redirect, send_file, current_app, jsonify
from forms import LoginForm
from models import Post, User, KumpulTugas
from models.others import Phile
from werkzeug.utils import secure_filename


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
    return render_template('home.html', posts=posts)

def blog_detail(post_id):
    return 'blog detail'


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
