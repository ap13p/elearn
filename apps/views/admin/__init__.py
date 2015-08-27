from flask import redirect, url_for

from apps.views.admin.matkul import (matkul_create, matkul_delete, matkul_list, matkul_update)
from apps.views.admin.user import (user_list, user_create, user_delete, user_update)
from apps.views.admin.post import (post_delete, post_create, post_list, post_update)
from apps.decorators import admin_required


@admin_required
def home():
    return redirect(url_for('admin:post:list'))
