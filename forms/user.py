from flask_wtf.form import Form
from models import Level
from wtforms.fields import StringField, PasswordField, SelectField
from wtforms.fields.html5 import EmailField, TelField, DateField
from wtforms.validators import input_required
from . import CKEditorField


def get_level():
    return [(level.id, level.name) for level in Level.select()]


class UserForm(Form):
    no_induk = StringField(validators=[input_required()])
    name = StringField(validators=[input_required()])
    email = EmailField(validators=[input_required()])
    password = PasswordField(validators=[input_required()])
    no_telpon = TelField()
    tanggal_lahir = DateField(validators=[input_required()])
    level = SelectField(coerce=int)
    alamat = CKEditorField(validators=[input_required()])


class LevelForm(Form):
    name = StringField(validators=[input_required()])
