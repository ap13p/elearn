from flask_wtf.form import Form
from models import User, Level, MataKuliah
from wtforms.fields import StringField, SelectField, BooleanField, FileField
from wtforms.fields.html5 import DateField
from wtforms.validators import input_required, optional
from . import CKEditorField


def get_dosen():
    level = Level.select().where(Level.name == 'dosen')
    users = [(user.id, user.name) for user in User.select().where(User.level == level)]
    return users


def get_matkul():
    matkuls = [(matkul.id, matkul.name) for matkul in MataKuliah.select()]
    return matkuls


class MataKuliahForm(Form):
    kode = StringField(validators=[input_required()])
    judul = StringField(validators=[input_required()])
    dosen = SelectField(coerce=int)


class TugasForm(Form):
    judul = StringField(validators=[input_required()])
    keterangan = CKEditorField(validators=[optional()])
    tanggal_terakhir = DateField(validators=[input_required()])


class PostForm(Form):
    judul = StringField(validators=[input_required()])
    konten = CKEditorField(validators=[input_required()])
    publik = BooleanField(validators=[optional()], default=True)

class KumpulkanTugasForm(Form):
    phile = FileField(label='File', validators=[input_required()])
