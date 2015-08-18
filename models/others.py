__author__ = 'Afief'

from datetime import datetime
from . import db
from peewee import CharField, TextField, BooleanField, ForeignKeyField, DateField
from models.auth import User


class Post(db.Model):
    judul = CharField(max_length=100)
    konten = TextField()
    publik = BooleanField(default=True)


class MataKuliah(db.Model):
    kode = CharField(max_length=5)
    judul = CharField(max_length=20)
    dosen = ForeignKeyField(User)


class Tugas(db.Model):
    judul = CharField(max_length=20)
    keterangan = TextField(null=True)
    mata_kuliah = ForeignKeyField(MataKuliah)
    tanggal_terakhir = DateField()


class KumpulTugas(db.Model):
    tugas = ForeignKeyField(Tugas)
    mahasiswa = ForeignKeyField(User)
    tanggal_mengumpulkan = DateField(default=datetime.now)
    file_path = TextField()


class UploadTugas(db.Model):
    tugas = ForeignKeyField(Tugas)
    file_path = CharField(max_length=255)
