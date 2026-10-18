import mysql.connector
import time
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='data_siswa'
)
ask = input("Create table nilai (y/N)")
if ask == "y" or ask =="Y":
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE nilai_siswa (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nis VARCHAR(20) NOT NULL,
        mapel VARCHAR(30) NOT NULL,
        nilai_tugas INT NOT NULL,
        nilai_uts INT NOT NULL,
        nilai_uas INT NOT NULL,
        nilai_akhir FLOAT NOT NULL,
        FOREIGN KEY (nis) REFERENCES siswa(nis)
    )
    """)
    print("Tabel Nilai Siswa berhasil dibuat")

print("="*36)
print(" "*15+"OPTION"+" "*15)
print("="*36)
print ("1. View")
print ("2. Insert nilai (preset)")
print ("3. Update (preset)")
print ("31. Insert nilai (manual)")
print ("4. Delete")
print ("5. exit")

opt = int(input("OPT:"))
print("="*36)
if opt == 1:
    cursor = conn.cursor()
    query = """
        SELECT siswa.nis, siswa.nama_siswa, nilai_siswa.mapel,
            nilai_siswa.nilai_tugas, nilai_siswa.nilai_uts,
            nilai_siswa.nilai_uas, nilai_siswa.nilai_akhir
        FROM siswa
        JOIN nilai_siswa ON siswa.nis = nilai_siswa.nis
    """

    cursor.execute(query)
    hasil = cursor.fetchall()

    for baris in hasil:
        print(baris)
elif opt == 2 :
    cursor = conn.cursor()
    query = "INSERT INTO nilai_siswa (nis, mapel, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir) VALUES (%s, %s, %s, %s, %s, %s)"
    data = [
        ("20219001", "Basis Data", 85, 80, 88, 84.3),
        ("20219002", "Basis Data", 90, 85, 92, 89.2),
        ("20219003", "Basis Data", 75, 78, 80, 77.5)
    ]

    cursor.executemany(query, data)
    conn.commit()

    print("Data Nilai Siswa berhasil di rekam")
elif opt == 31:
    cursor = conn.cursor()
    nis_input = input("Masukkan NIS siswa: ")
    mapel_input = input("Masukkan mata pelajaran: ")
    nilai_tugas_input = int(input("Masukkan nilai tugas: "))
    nilai_uts_input = int(input("Masukkan nilai UTS: "))
    nilai_uas_input = int(input("Masukkan nilai UAS: "))
    nilai_akhir_input = float(input("Masukkan nilai akhir: "))

    query = "INSERT INTO nilai_siswa (nis, mapel, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir) VALUES (%s, %s, %s, %s, %s, %s)"
elif opt == 3 :
    cursor = conn.cursor()
    
    query = "UPDATE nilai_siswa SET nilai_uas = %s, nilai_akhir = %s WHERE nis = %s AND mapel = %s"
    data = (90, 87.5, "20219001", "Basis Data")
    
    cursor.execute(query, data)
    conn.commit()
    print(cursor.rowcount, "Data nilai berhasil diubah")
elif opt == 4: #DELETE
    cursor = conn.cursor(buffered=True)
    while True:
        nis_del = int(input("Masukan NIS valid yang ingin dihapus:"))
        existence = "SELECT 1 FROM nilai_siswa WHERE nis = %s"
        cursor.execute(existence, (nis_del,))
        if cursor.fetchone():
            confirm_del = input("ARE YOU SURE TO DELETE THIS DATA? (y/N): ")
            if confirm_del.lower() == 'y':
                query = "DELETE FROM nilai_siswa WHERE nis = %s"
                cursor.execute(query, (nis_del,))
                conn.commit()
                for seconds in range(4, 0, -1):
                    print(f"Deleting data in {seconds} seconds...", end="\r")
                    time.sleep(1)
                print(cursor.rowcount, "Data nilai berhasil dihapus")
            break
        else:
            print("NIS tidak valid. Harap masukkan NIS 8 digit.")
else:
    print("thanks")