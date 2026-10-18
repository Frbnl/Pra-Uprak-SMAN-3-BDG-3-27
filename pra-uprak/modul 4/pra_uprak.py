import mysql.connector
import time

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="swalayanif1"
)
dbcursor = conn.cursor()

def timer(a):
    for seconds in range(a, 0, -1):
                    print(f"Moving in {seconds} seconds...", end="\r")
                    time.sleep(1)
    
def tampilkan(sql, parameter=None):
    if parameter:
        dbcursor.execute(sql, parameter)
    else:
        dbcursor.execute(sql)
    
    data = dbcursor.fetchall()
    if not data:
        print("Tidak ada data ditemukan.")
    else:
        for row in data:
            print(row)


while True:
    print("\n=== MENU UPRAK SWALAYAN ===")
    print("1. Tampilkan Semua Produk")
    print("2. Produk + Supplier (INNER JOIN)")
    print("3. Supplier + Produk (LEFT JOIN)")
    print("4. Supplier + Produk (RIGHT JOIN)")
    print("5. Filter Produk (Stok > 10)")
    print("6. Update Stok Produk")
    print("0. Keluar")
    
    pilihan = input("Pilihan: ")

    if pilihan == "1":
        print("\n--- DAFTAR PRODUK ---")
        tampilkan("""
            SELECT id, kode_produk, nama_produk, harga, stok 
            FROM produk
        """)

    elif pilihan == "2":
        print("\n--- INNER JOIN (PRODUK & SUPPLIER) ---")
        tampilkan("""
            SELECT p.kode_produk, p.nama_produk, s.nama AS supplier
            FROM produk p
            INNER JOIN supplier s ON p.supplier_id = s.id
        """)
        timer(3)
    elif pilihan == "3":
        print("\n--- LEFT JOIN (SUPPLIER & PRODUK) ---")
        tampilkan("""
            SELECT s.nama AS supplier, p.kode_produk, p.nama_produk
            FROM supplier s
            LEFT JOIN produk p ON p.supplier_id = s.id
        """)

    elif pilihan == "4":
        print("\n--- RIGHT JOIN (PRODUK & SUPPLIER) ---")
        tampilkan("""
            SELECT s.nama AS supplier, p.kode_produk, p.nama_produk
            FROM produk p
            RIGHT JOIN supplier s ON p.supplier_id = s.id
        """)

    elif pilihan == "5":
        print("\n--- PRODUK DENGAN STOK > 10 ---")
        tampilkan("""
            SELECT id, kode_produk, nama_produk, stok
            FROM produk
            WHERE stok > %s
        """, (10,))

    elif pilihan == "6":
        print("\n--- UPDATE STOK PRODUK ---")
        try:
            id_produk = int(input("Masukkan ID produk yang akan diupdate: "))
            
            print("\nKondisi SEBELUM update:")
            tampilkan("SELECT id, kode_produk, nama_produk, stok FROM produk WHERE id = %s", (id_produk,))
            
            tambahan = int(input("Tambahan jumlah stok: "))
            
            sql_update = "UPDATE produk SET stok = stok + %s WHERE id = %s"
            dbcursor.execute(sql_update, (tambahan, id_produk))
            conn.commit()
            print(">>> Data berhasil diperbarui! <<<")
            
            print("Kondisi SESUDAH update:")
            tampilkan("SELECT id, kode_produk, nama_produk, stok FROM produk WHERE id = %s", (id_produk,))
        except ValueError:
            print("Input harus berupa angka!")
        except mysql.connector.Error as err:
            print(f"Terjadi kesalahan database: {err}")

    elif pilihan == "0":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")

dbcursor.close()
conn.close()
print("Program selesai.")