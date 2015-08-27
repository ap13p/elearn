from models import *

level = [{
    'name': 'admin'
}, {
    'name': 'dosen'
}, {
    'name': 'mahasiswa'
}]
user = [{
    'name': 'Admin 1',
    'password': 'qwe123',
    'email': 'admin1@gmail.com',
    'alamat': 'Jl. Admin 1',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '1001',
    'jenkel': 'L',
    'level': 'admin'
}, {
    'name': 'Admin 2',
    'password': 'qwe123',
    'email': 'admin2@gmail.com',
    'alamat': 'Jl. Admin 2',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '1002',
    'jenkel': 'P',
    'level': 'admin'
}, {
    'name': 'Admin 3',
    'password': 'qwe123',
    'email': 'admin3@gmail.com',
    'alamat': 'Jl. Admin 3',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '1003',
    'jenkel': 'L',
    'level': 'admin'
}, {  ###### Dosen
    'name': 'Dosen 1',
    'password': 'qwe123',
    'email': 'dosen1@gmail.com',
    'alamat': 'Jl. Dosen 1',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '2001',
    'jenkel': 'P',
    'level': 'dosen'
}, {
    'name': 'Dosen 2',
    'password': 'qwe123',
    'email': 'dosen2@gmail.com',
    'alamat': 'Jl. Dosen 2',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '2002',
    'jenkel': 'L',
    'level': 'dosen'
}, {
    'name': 'Dosen 3',
    'password': 'qwe123',
    'email': 'dosen3@gmail.com',
    'alamat': 'Jl. Dosen 3',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '2003',
    'jenkel': 'L',
    'level': 'dosen'
},{  ############ MAHASISWA
    'name': 'Mahasiswa 1',
    'password': 'qwe123',
    'email': 'mhs1@gmail.com',
    'alamat': 'Jl. Mahasiswa 1',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '3001',
    'jenkel': 'P',
    'level': 'mahasiswa'
}, {
    'name': 'Mahasiswa 2',
    'password': 'qwe123',
    'email': 'mhs2@gmail.com',
    'alamat': 'Jl. Mahasiswa 2',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '3002',
    'jenkel': 'P',
    'level': 'mahasiswa'
}, {
    'name': 'Mahasiswa 3',
    'password': 'qwe123',
    'email': 'mhs3@gmail.com',
    'alamat': 'Jl. Mahasiswa 3',
    'no_telpon': '0321-362780',
    'tanggal_lahir': '1980-03-27',
    'no_induk': '3003',
    'jenkel': 'L',
    'level': 'mahasiswa'
}]

matkul = [{
    'kode': 'k001',
    'judul': 'Database',
    'dosen': 'dosen1@gmail.com'
}, {
    'kode': 'k002',
    'judul': 'Jaringan',
    'dosen': 'dosen2@gmail.com'
}, {
    'kode': 'k003',
    'judul': 'DFD',
    'dosen': 'dosen3@gmail.com'
}]


def seed_it(_db):
    global level, matkul, user

    with _db.atomic():
        Level.insert_many(level).execute()

        # Insert admin
        for data in user:
            p = Profile()
            p.nama = data['name']
            p.jenis_kelamin = data['jenkel']
            p.no_telpon = data['no_telpon']
            p.tanggal_lahir = data['tanggal_lahir']
            p.alamat = data['alamat']
            p.save()

            u = User()
            u.email = data['email']
            u.password = data['password']
            u.no_induk = data['no_induk']
            u.level = Level.get(Level.name == data['level'])
            u.profile = p
            u.save()

        for data in matkul:
            m = MataKuliah()
            m.kode = data['kode']
            m.judul = data['judul']
            m.dosen = User.get(User.email == data['dosen'])
            m.save()
