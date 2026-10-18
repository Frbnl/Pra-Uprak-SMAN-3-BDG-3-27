import mysql.connector

def buat_database():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )
    if db.is_connected():
        print('Konek Database Mysql Berhasil')
        buat = db.cursor()
        buat.execute("CREATE DATABASE data_siswa")
        print("DATABASE Berhasil dibuat !")
    else:
        print('Koneksi Gagal')

def buat_tabel():
    konek = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='data_siswa'
    )
    cursors = konek.cursor()
    cursors.execute(
    """
    CREATE TABLE siswa (
    nis VARCHAR(20) PRIMARY KEY,
    nisn VARCHAR(20) NOT NULL,
    nama_siswa VARCHAR(30) NOT NULL,
    jenis_kelamin VARCHAR(5) NOT NULL,
    tgl_lahir date NOT NULL,
    kelas VARCHAR(10) NOT NULL,
    status INT(4) NOT NULL
    )
    """
    )
    print('Tabel Siswa Berhasil dibuat')

def insert_data():
    konek = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='data_siswa'
    )
    cursor = konek.cursor()
    query = "INSERT INTO siswa (nis,nisn,nama_siswa,jenis_kelamin,tgl_lahir,kelas,status) VALUES(%s, %s, %s,%s,%s,%s,%s)"
    data = [("20219001", "01234567", "Ardiansyah", "L", "2 Maret 1996", "10 MIPA 1", "Aktif"),
            ("20219002", "01234564", "Sherina", "P", "5 Agustus 1997", "10 MIPA 1", "Aktif"),
            ("20219003", "01234568", "Fitra Ery", "L", "11 Juni 1997", "10 MIPA 1", "Aktif")]

    cursor.executemany(query, data)
    konek.commit()
    print("Data Nilai Siswa berhasil di rekam")

# Menu Opsi
while True:
    print("\n--- MENU KONEKSI DATABASE ---")
    print("1. Buat Database")
    print("2. Buat Tabel (Preset)")
    print("3. Insert Data (Preset)")
    print("4. Exit")
    
    pilih = input("Pilih menu (1-4): ")

    if pilih == '1':
        buat_database()
    elif pilih == '2':
        buat_tabel()
    elif pilih == '3':
        insert_data()
    elif pilih == '4':
        print("Selesai.")
        break
    else:
        print("Pilihan tidak valid!")