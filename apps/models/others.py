__author__ = 'Afief'

from datetime import datetime
from peewee import CharField, TextField, BooleanField, ForeignKeyField, DateField

from apps.models import db
from apps.models.auth import User


class Phile(db.Model):
    filename = CharField(max_length=100)
    filetype = CharField(max_length=100)
    filepath = TextField()

class Post(db.Model):
    judul = CharField(max_length=100)
    konten = TextField()
    date_created = DateField(default=datetime.now)
    publik = BooleanField(default=True)

    class Meta:
        order_by = ('-date_created',)


class MataKuliah(db.Model):
    kode = CharField(max_length=5)
    judul = CharField(max_length=20)
    dosen = ForeignKeyField(User)

    class Meta:
        order_by = ('kode',)


class Tugas(db.Model):
    judul = CharField(max_length=20)
    keterangan = TextField(null=True)
    mata_kuliah = ForeignKeyField(MataKuliah)
    tanggal_terakhir = DateField()

    class Meta:
        order_by = ('-id',)

class KumpulTugas(db.Model):
    tugas = ForeignKeyField(Tugas)
    mahasiswa = ForeignKeyField(User)
    tanggal_mengumpulkan = DateField(default=datetime.now)
    phile = ForeignKeyField(Phile)

    class Meta:
        order_by = ('-tanggal_mengumpulkan',)

