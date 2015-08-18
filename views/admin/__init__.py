from flask import render_template

from matkul import (matkul_create, matkul_delete, matkul_list, matkul_update)
from tugas import (tugas_list, tugas_create, tugas_delete, tugas_update, kumpul_tugas, sudah_mengumpulkan_tugas)
from user import (user_list, user_create, user_delete, user_update)
from post import (post_delete, post_create, post_list, post_update)
from decorators import admin_required


@admin_required
def home():
    return render_template('admin/home.html')
