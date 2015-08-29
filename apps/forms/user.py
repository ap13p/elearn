from flask_wtf.form import Form
from wtforms.fields import FileField
from wtforms.fields import StringField, PasswordField, SelectField, FormField, TextAreaField
from wtforms.fields.html5 import EmailField, TelField, DateField
from wtforms.validators import input_required, optional, regexp, equal_to

from apps.models import Level

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
    jenis_kelamin = SelectField(coerce=str, choices=jenkel_choices,
                                validators=[input_required()])


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


class ChangePasswordForm(Form):
    password_lama = PasswordField(validators=[input_required()],
                                  label='Password lama')
    password_baru = PasswordField(validators=[input_required()],
                                  label='Password baru')
    password_konfirm = PasswordField(
        validators=[equal_to('password_baru',
                             message='Harus sama dengan field password baru')],
        label='Konfirmasi password'
    )
