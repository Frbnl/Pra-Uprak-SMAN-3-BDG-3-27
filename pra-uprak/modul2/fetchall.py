import mysql.connector

konek = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='data_siswa'
)

dbcursor = konek.cursor()
sql = "SELECT * FROM siswa WHERE kelas = '10 MIPA 1'"
dbcursor.execute(sql)
dt = dbcursor.fetchall()

for data in dt:
    print(data)

konek.close()