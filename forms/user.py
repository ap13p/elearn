from flask_wtf.form import Form
# from flask_wtf.file import FileAllowed
from models import Level
from wtforms.fields import FileField
from wtforms.fields import StringField, PasswordField, SelectField, FormField, TextAreaField
from wtforms.fields.html5 import EmailField, TelField, DateField
from wtforms.validators import input_required, optional, regexp
from . import CKEditorField

jenkel_choices = (
    ('L', 'Laki-laki'),
    ('P', 'Perempuan')
)


def get_level():
    return [(level.id, level.name) for level in Level.select()]


class ProfileForm(Form):
    image = FileField(validators=[
        optional(),
        regexp(u'(.+)(?:.jpe?g|png)$')
    ], label='Foto')
    nama = StringField(validators=[input_required()])
    no_telpon = TelField(validators=[optional()])
    tanggal_lahir = DateField(validators=[optional()])
    alamat = TextAreaField(validators=[optional()])
    jenis_kelamin = SelectField(coerce=str, choices=jenkel_choices, validators=[input_required()])


class UserForm(Form):
    no_induk = StringField(validators=[input_required()])
    email = EmailField(validators=[input_required()])
    password = PasswordField(validators=[input_required()])
    level = SelectField(coerce=int)
    profile = FormField(ProfileForm)


class LevelForm(Form):
    name = StringField(validators=[input_required()])


class UpdateInfoForm(Form):
    email = EmailField()
    no_induk = StringField()
    profile = FormField(ProfileForm)
