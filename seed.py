from app import create_app
from models import *


create_app()

level_admin = Level.create(name='admin')
level_dosen = Level.create(name='dosen')
level_mhs = Level.create(name='mahasiswa')

user_admin1 = User.create(
    name='Admin 1',
    password='qwe123',
    email='admin1@gmail.com',
    level=level_admin,
    alamat='Admin 1',
    no_telpon='0321-362780',
    tanggal_lahir='1994-09-23',
    no_induk='12345'
)
user_admin2 = User.create(
    name='Admin 2',
    password='qwe123',
    email='admin2@gmail.com',
    level=level_admin,
    alamat='Admin 2',
    no_telpon='0321-362780',
    tanggal_lahir='1994-09-23',
    no_induk='12346'
)
user_admin3 = User.create(
    name='Admin 3',
    password='qwe123',
    email='admin3@gmail.com',
    level=level_admin,
    alamat='Admin 3',
    no_telpon='0321-362780',
    tanggal_lahir='1994-09-23',
    no_induk='12347'
)

user_dosen1 = User.create(
    name='Dosen 1',
    password='qwe123',
    email='dosen1@gmail.com',
    level=level_dosen,
    alamat='Dosen 1',
    no_telpon='0321-278090',
    tanggal_lahir='1990-02-24',
    no_induk='1234567'
)
user_dosen2 = User.create(
    name='Dosen 2',
    password='qwe123',
    email='dosen2@gmail.com',
    level=level_dosen,
    alamat='Dosen 2',
    no_telpon='0321-278090',
    tanggal_lahir='1990-02-24',
    no_induk='1234568'
)
user_dosen3 = User.create(
    name='Dosen 3',
    password='qwe123',
    email='dosen3@gmail.com',
    level=level_dosen,
    alamat='Dosen 3',
    no_telpon='0321-278090',
    tanggal_lahir='1990-02-24',
    no_induk='1234569'
)
user_dosen4 = User.create(
    name='Dosen 4',
    password='qwe123',
    email='dosen4@gmail.com',
    level=level_dosen,
    alamat='Dosen 4',
    no_telpon='0321-278090',
    tanggal_lahir='1990-02-24',
    no_induk='1234570'
)

matkul1 = MataKuliah.create(
    kode='kod001',
    judul='Database',
    dosen=user_dosen1
)
matkul2 = MataKuliah.create(
    kode='kod002',
    judul='Jaringan',
    dosen=user_dosen2
)
matkul3 = MataKuliah.create(
    kode='kod003',
    judul='DFD',
    dosen=user_dosen3
)
matkul4 = MataKuliah.create(
    kode='kod004',
    judul='VB',
    dosen=user_dosen4
)

mhs1 = User.create(
    name='Mahasiswa 1',
    email='mhs1@gmail.com',
    password='qwe123',
    level=level_mhs,
    alamat='Mahasiswa 1',
    no_telpon='082143103864',
    tanggal_lahir='1996-09-20',
    no_induk='23001'
)
mhs2 = User.create(
    name='Mahasiswa 2',
    email='mhs2@gmail.com',
    password='qwe123',
    level=level_mhs,
    alamat='Mahasiswa 2',
    no_telpon='082143103864',
    tanggal_lahir='1996-09-20',
    no_induk='23002'
)
mhs3 = User.create(
    name='Mahasiswa 3',
    email='mhs3@gmail.com',
    password='qwe123',
    level=level_mhs,
    alamat='Mahasiswa 3',
    no_telpon='082143103864',
    tanggal_lahir='1996-09-20',
    no_induk='23003'
)
mhs4 = User.create(
    name='Mahasiswa 4',
    email='mhs4@gmail.com',
    password='qwe123',
    level=level_mhs,
    alamat='Mahasiswa 4',
    no_telpon='082143103864',
    tanggal_lahir='1996-09-20',
    no_induk='23004'
)


def seed_it():
    pass
