from flask_bcrypt import generate_password_hash, check_password_hash
from peewee import CharField, TextField, DateField, ForeignKeyField
from playhouse.signals import Model, pre_save

from apps.models import db

class Level(db.Model):
    name = CharField(max_length=20)

class Profile(db.Model):
    nama = CharField(max_length=60)
    alamat = TextField(null=True)
    tanggal_lahir = DateField(null=True)
    no_telpon = CharField(max_length=20, null=True)
    jenis_kelamin = CharField(max_length=1)
    image = TextField(null=True, default='/static/img/default-account.jpg')

class User(db.Model, Model):
    email = CharField(max_length=100)
    password = CharField(max_length=60)
    level = ForeignKeyField(Level)
    no_induk = CharField(max_length=20)
    profile = ForeignKeyField(Profile)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_password(self, raw_password):
        return generate_password_hash(raw_password)

    class Meta:
        order_by = ('-no_induk',)


@pre_save(sender=User)
def on_pre_save_user(model_cls, instance, created):
    instance.password = generate_password_hash(instance.password)
