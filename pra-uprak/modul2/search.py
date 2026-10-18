import mysql.connector

konek = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='data_siswa'
)

dbcursor = konek.cursor()
kelas = input("Masukkan kelas yang ingin dicari: ")

sql = "SELECT * FROM siswa WHERE kelas = %s"
dbcursor.execute(sql, (kelas,))

dt = dbcursor.fetchall()

print("\nData siswa:")
for data in dt:
    print(data)

konek.close()