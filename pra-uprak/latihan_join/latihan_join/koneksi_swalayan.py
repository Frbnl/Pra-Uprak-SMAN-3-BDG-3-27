import mysql.connector

konek = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="swalayanIF1"
)
dbcursor = konek.cursor()

def tampilkan(sql, parameter=None):
    dbcursor.execute(sql, parameter)
    print(" | ".join(dbcursor.column_names))
    print("-" * 60)
    for baris in dbcursor.fetchall():
        print(" | ".join("NULL" if x is None else str(x) for x in baris))
