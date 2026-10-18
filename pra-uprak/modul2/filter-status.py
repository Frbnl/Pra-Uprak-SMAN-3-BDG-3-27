import mysql.connector

konek = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='data_siswa'
)

dbcursor = konek.cursor()
sql = "SELECT * FROM siswa WHERE Status = 'Aktif'"
dbcursor.execute(sql)
dt = dbcursor.fetchall()

for data in dt:
    print(data)

konek.close()