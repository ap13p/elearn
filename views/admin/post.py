from flask_peewee.utils import object_list
from flask import redirect, g, url_for, flash, request, render_template
from forms.others import PostForm
from models import Post, User
from decorators import admin_required


@admin_required
def post_list():
    posts = Post.select()
    return object_list('admin/post/list.html', posts, var_name='posts', paginate_by=10)

@admin_required
def post_create():
    form = PostForm(request.form)
    form.action = url_for('admin:post:create')
    if form.validate_on_submit():
        post = Post()
        form.populate_obj(post)
        post.save()
        flash('Sukses membuat posting baru')
        return redirect(url_for('admin:post:list'))
    return render_template('admin/post/create.html', form=form)

@admin_required
def post_update(post_id):
    post = Post.get(Post.id == post_id)
    form = PostForm(request.form, obj=post)
    form.action = url_for('admin:post:update', post_id=post_id)
    if form.validate_on_submit():
        form.populate_obj(post)
        post.save()
        flash('Sukses memperbarui posting')
        return redirect(url_for('admin:post:list'))
    return render_template('admin/post/update.html', form=form)

@admin_required
def post_delete(post_id):
    if g.user and g.user.level.name == 'admin':
        post = None
        try:
            post = Post.get(Post.id == post_id)
        except Post.DoesNotExist:
            flash('Gagal menghapus posting')
        if post:
            post.delete_instance()
            flash('Sukses menghapus posting')
        return redirect(url_for('admin:post:list'))
