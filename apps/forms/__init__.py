from flask_wtf.form import Form
from wtforms.fields import TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.widgets.core import TextArea
from wtforms.validators import input_required


class CKEditorWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += 'ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKEditorWidget, self).__call__(field, **kwargs)


class CKEditorField(TextAreaField):
    widget = CKEditorWidget()


class LoginForm(Form):
    email = EmailField(validators=[input_required()])
    password = PasswordField(validators=[input_required()])


__all__ = ('LoginForm', 'CKEditorField')
