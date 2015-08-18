from flask import render_template, request, flash, session, url_for, redirect, send_file
from forms import LoginForm
from models import Post, User, KumpulTugas

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
    kt = KumpulTugas.get(KumpulTugas.id == file_id)
    filepath = kt.file_path
    download = bool(request.args.get('download', False))
    return send_file(filepath, as_attachment=download)
