from werkzeug.utils import secure_filename
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
      'name': 'Yunan Irmantono,M.Pd',
      'password': 'qwe123',
      'email': 'yunan@gmail.com',
      'no_induk': '23011',
      'jenkel': 'L',
      'level': 'dosen',
      'k_matkul': 'k001',
      'k_judul': 'Matematika Diskrit'
      }, {
    'name': 'Ali Basyah,ST,M.Pd',
    'password': 'qwe123',
    'email': 'ali.basyah@gmail.com',
    'no_induk': '23012',
    'jenkel': 'L',
    'level': 'dosen',
    'k_matkul': 'k002',
    'k_judul': 'Pengenalan Dasar Komputer dan Internet'
}, {
    'name': 'Khoirul Ikhsan Fakeh,S.ST',
    'password': 'qwe123',
    'email': 'khoifa@gmail.com',
    'no_induk': '23013',
    'jenkel': 'L',
    'level': 'dosen',
    'k_matkul': 'k003',
    'k_judul': 'Desain Web'
}, {
    'name': 'Vera Kusumaningrum,S.Kom',
    'password': 'qwe123',
    'email': 'vera.k@gmail.com',
    'no_induk': '23014',
    'jenkel': 'P',
    'level': 'dosen',
    'k_matkul': 'k004',
    'k_judul': 'Program Aplikasi Bisnis dan Perkantoran'
}, {
    'name': 'Ali Hamzah,S.Kom',
    'password': 'qwe123',
    'email': 'ali.ham@gmail.com',
    'no_induk': '23015',
    'jenkel': 'L',
    'level': 'dosen',
    'k_matkul': 'k005',
    'k_judul': 'Algoritma Pemrograman'
}, {
    'name': 'Mohammad Khoiron,S.Kom',
    'password': 'qwe123',
    'email': 'khoiron@gmail.com',
    'no_induk': '23016',
    'jenkel': 'L',
    'level': 'dosen',
    'k_matkul': 'k006',
    'k_judul': 'Database'
}, {
    'name': 'Choirul Anwar,M.Pd',
    'password': 'qwe123',
    'email': 'choi@gmail.com',
    'no_induk': '23017',
    'jenkel': 'L',
    'level': 'dosen',
    'k_matkul': 'k007',
    'k_judul': 'Konsep Jaringan Komputer'
}, {
    'name': 'Ahmad Doni Prasetyo,S.ST',
    'password': 'qwe123',
    'email': 'a.doni@gmail.com',
    'no_induk': '23018',
    'jenkel': 'L',
    'level': 'dosen',
    'k_matkul': 'k008',
    'k_judul': 'Merakit, Perawatan dan Perbaikan PC'
}, {
    'name': 'Heru Susanto,S.Pd',
    'password': 'qwe123',
    'email': 'eruh@gmail.com',
    'no_induk': '23019',
    'jenkel': 'L',
    'level': 'dosen',
    'k_matkul': 'k009',
    'k_judul': 'Bahasa Inggris'
}, {  # Mahasiswa
      'name': 'A.A Samsudin',
      'jenkel': 'L',
      'level': 'mhs'
      }, {
    'name': 'A.M Rizal',
    'jenkel': 'L',
    'level': 'mhs',
}, {
    'name': 'A.R Rais',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'A. Saifudin',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'Afief S',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'A.A Salahuddin',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'A. Nasrudin',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'A.F Rozi',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'Anggy R.A',
    'jenkel': 'L',
    'level': 'mhs',
}, {
    'name': 'Asmo S',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'Ayu Nur. O',
    'jenkel': 'P',
    'level': 'mhs'
}, {
    'name': 'Ayu R.P',
    'jenkel': 'P',
    'level': 'mhs'
}, {
    'name': 'Dian Affana',
    'jenkel': 'P',
    'level': 'mhs'
}, {
    'name': 'Dicky E.N',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'Eva P',
    'jenkel': 'P',
    'level': 'mhs'
}, {
    'name': 'Fairuz B',
    'jenkel': 'P',
    'level': 'mhs'
}, {
    'name': 'Fajar R.H.H',
    'jenkel': 'L',
    'level': 'mhs'
}, {
    'name': 'Hendra S.S',
    'jenkel': 'L',
    'level': 'mhs'
}]


def seed_it(_db):
    global level, user

    with _db.atomic():
        Level.insert_many(level).execute()

        # Insert admin
        indek = 1
        for data in user:
            p = Profile()
            p.nama = data['name']
            p.jenis_kelamin = data['jenkel']
            p.save()

            u = User()
            u.profile = p
            if data['level'] == 'mhs':
                u.level = Level.get(Level.name == 'mahasiswa')
                email = secure_filename(data['name'].lower()[0:5]) + \
                        '@gmail.com'
                u.email = email
                u.password = 'qwe123'
                u.no_induk = 7414120000 + indek
                u.save()
                indek += 1
            else:

                u.email = data['email']
                u.password = 'qwe123'
                if data.get('no_induk'):
                    u.no_induk = data['no_induk']
                u.level = Level.get(Level.name == data['level'])
                u.save()

                if data['level'] == 'dosen':
                    MataKuliah.create(
                        kode=data['k_matkul'],
                        judul=data['k_judul'],
                        dosen=u
                    )
