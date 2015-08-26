from flask import redirect, url_for

from matkul import (matkul_create, matkul_delete, matkul_list, matkul_update)
from user import (user_list, user_create, user_delete, user_update)
from post import (post_delete, post_create, post_list, post_update)
from decorators import admin_required


@admin_required
def home():
    return redirect(url_for('admin:post:list'))
