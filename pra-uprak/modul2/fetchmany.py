import mysql.connector

konek = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='data_siswa'
)

dbcursor = konek.cursor()
sql = "select * from siswa"
dbcursor.execute(sql)
dt = dbcursor.fetchmany(2)

for data in dt:
    print(data)