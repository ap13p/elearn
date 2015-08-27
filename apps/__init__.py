from flask import g, session, Flask
from flask_debugtoolbar import DebugToolbarExtension

from apps import config

app = Flask(__name__)
app.config.from_object(config)
toolbar = DebugToolbarExtension(app)

from apps.models import *


def create_app():
    db.init_app(app)
    db.database.create_tables([
        Post, KumpulTugas,
        Tugas, MataKuliah, Level,
        User, Phile, Profile
    ], safe=True)
    return app


def seed():
    db.init_app(app)
    db.database.drop_tables([
        Post, KumpulTugas, Tugas,
        MataKuliah, Level, User,
        Phile, Profile
    ], safe=True)
    db.database.create_tables([
        Post, KumpulTugas,
        Tugas, MataKuliah, Level,
        User, Phile, Profile
    ], safe=True)
    from apps.seed import seed_it
    seed_it(db.database)
    return app


from apps.views import (home, login, logout, blog_detail,
                   sendfile, upload, update_info,
                   media, change_password)
from apps.views.admin import (home as admin_home,
                         user_list as admin_user_list,
                         user_create as admin_user_create,
                         user_delete as admin_user_delete,
                         user_update as admin_user_update,
                         post_list as admin_post_list,
                         post_update as admin_post_update,
                         post_create as admin_post_create,
                         post_delete as admin_post_delete,
                         matkul_list as admin_matkul_list,
                         matkul_update as admin_matkul_update,
                         matkul_delete as admin_matkul_delete,
                         matkul_create as admin_matkul_create)
from apps.views.dosen import (home as dosen_home,
                         tugas_list as dosen_tugas_list,
                         tugas_create as dosen_tugas_create,
                         tugas_update as dosen_tugas_update,
                         tugas_delete as dosen_tugas_delete,
                         tugas_detail as dosen_tugas_detail)

from apps.views.mhs import (home as mhs_home,
                       tugas_detail as mhs_tugas_detail,
                       tugas_kumpulkan as mhs_tugas_kumpulkan)


app.add_url_rule('/logout/', 'logout', logout)
app.add_url_rule('/login/', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/sendfile/<int:file_id>/', 'sendfile', sendfile)
app.add_url_rule('/media/<path:filepath>/', 'media', media)
app.add_url_rule('/upload/', 'upload', upload, methods=['POST'])
app.add_url_rule('/update-info/<int:user_id>/', 'update-info', update_info, methods=['GET', 'POST'])
app.add_url_rule('/change-password/<int:user_id>/', 'change-password', change_password, methods=['GET', 'POST'])

app.add_url_rule('/', 'home', home)
app.add_url_rule('/detail/<int:post_id>/', 'post:detail', blog_detail)

app.add_url_rule('/admin/', 'admin:home', admin_home)

app.add_url_rule('/admin/user/list/', 'admin:user:list', admin_user_list)
app.add_url_rule('/admin/user/create/', 'admin:user:create', admin_user_create, methods=['GET', 'POST'])
app.add_url_rule('/admin/user/update/<int:user_id>/', 'admin:user:update', admin_user_update, methods=['GET', 'POST'])
app.add_url_rule('/admin/user/delete/<int:user_id>/', 'admin:user:delete', admin_user_delete)
app.add_url_rule('/admin/post/list/', 'admin:post:list', admin_post_list)
app.add_url_rule('/admin/post/create/', 'admin:post:create', admin_post_create, methods=['GET', 'POST'])
app.add_url_rule('/admin/post/update/<int:post_id>/', 'admin:post:update', admin_post_update, methods=['GET', 'POST'])
app.add_url_rule('/admin/post/delete/<int:post_id>/', 'admin:post:delete', admin_post_delete)
app.add_url_rule('/admin/matakuliah/list/', 'admin:matkul:list', admin_matkul_list)
app.add_url_rule('/admin/matakuliah/create/', 'admin:matkul:create', admin_matkul_create, methods=['GET', 'POST'])
app.add_url_rule('/admin/matakuliah/update/<int:matkul_id>/', 'admin:matkul:update', admin_matkul_update,
                 methods=['GET', 'POST'])
app.add_url_rule('/admin/matakuliah/delete/<int:matkul_id>/', 'admin:matkul:delete', admin_matkul_delete)

app.add_url_rule('/dosen/', 'dosen:home', dosen_home)
app.add_url_rule('/dosen/tugas/detail/<int:tugas_id>/', 'dosen:tugas:detail', dosen_tugas_detail)
app.add_url_rule('/dosen/tugas/create/', 'dosen:tugas:create', dosen_tugas_create, methods=['GET', 'POST'])
app.add_url_rule('/dosen/tugas/', 'dosen:tugas:list', dosen_tugas_list)
app.add_url_rule('/dosen/tugas/update/<int:tugas_id>/', 'dosen:tugas:update', dosen_tugas_update,
                 methods=['GET', 'POST'])
app.add_url_rule('/dosen/tugas/delete/<int:tugas_id>/', 'dosen:tugas:delete', dosen_tugas_delete)

app.add_url_rule('/mhs/', 'mhs:home', mhs_home)
app.add_url_rule('/mhs/detail/<int:tugas_id>/', 'mhs:tugas:detail', mhs_tugas_detail)
app.add_url_rule('/mhs/kumpul/<int:tugas_id>/', 'mhs:tugas:kumpulkan', mhs_tugas_kumpulkan, methods=['POST'])


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.get(User.id == session['user_id'])


from apps.filters import to_datetime
app.add_template_filter(to_datetime, 'datetime')
