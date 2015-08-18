__author__ = 'Afief'

from flask_bcrypt import generate_password_hash, check_password_hash
from . import db
from peewee import CharField, TextField, DateField, ForeignKeyField
from playhouse.signals import Model, pre_save

class Level(db.Model):
    name = CharField(max_length=20)


class User(db.Model, Model):
    name = CharField(max_length=60)
    email = CharField(max_length=100)
    password = CharField(max_length=60)
    level = ForeignKeyField(Level)
    alamat = TextField()
    no_telpon = CharField(max_length=20)
    tanggal_lahir = DateField()
    no_induk = CharField(max_length=20)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_password(self, raw_password):
        return generate_password_hash(raw_password)


@pre_save(sender=User)
def on_pre_save_user(model_cls, instance, created):
    instance.password = generate_password_hash(instance.password)
