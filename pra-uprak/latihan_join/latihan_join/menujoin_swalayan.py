from koneksi_swalayan import konek, dbcursor, tampilkan

while True:
    print("\n=== MENU JOIN SWALAYAN ===")
    print("1. Produk + supplier (INNER JOIN)")
    print("2. Nota penjualan lengkap (INNER JOIN 4 tabel)")
    print("3. Supplier + produk (LEFT JOIN)")
    print("4. Pelanggan yang belum pernah belanja (LEFT JOIN)")
    print("5. Supplier + produk (RIGHT JOIN)")
    print("6. Cari produk berdasarkan nama supplier")
    print("0. Keluar")
    pilihan = input("Pilihan: ")

    if pilihan == "1":
        tampilkan("""
            SELECT p.kode_produk, p.nama_produk, s.nama AS supplier
            FROM produk AS p
            INNER JOIN supplier AS s ON p.supplier_id = s.id
        """)
    elif pilihan == "2":
        tampilkan("""
            SELECT pj.id AS no_nota, pj.tanggal, pl.nama AS pelanggan,
                   p.nama_produk, pd.kuantitas, pd.total
            FROM penjualan_detail AS pd
            INNER JOIN penjualan AS pj ON pd.penjualan_id = pj.id
            INNER JOIN pelanggan AS pl ON pj.pelanggan_id = pl.id
            INNER JOIN produk AS p ON pd.produk_id = p.id
            ORDER BY pj.id
        """)
    elif pilihan == "3":
        tampilkan("""
            SELECT s.nama AS supplier, p.kode_produk, p.nama_produk
            FROM supplier AS s
            LEFT JOIN produk AS p ON p.supplier_id = s.id
        """)
    elif pilihan == "4":
        tampilkan("""
            SELECT pl.id, pl.nama, pl.telpon
            FROM pelanggan AS pl
            LEFT JOIN penjualan AS pj ON pj.pelanggan_id = pl.id
            WHERE pj.id IS NULL
        """)
    elif pilihan == "5":
        tampilkan("""
            SELECT s.nama AS supplier, p.kode_produk, p.nama_produk
            FROM produk AS p
            RIGHT JOIN supplier AS s ON p.supplier_id = s.id
        """)
    elif pilihan == "6":
        kata = input("Nama supplier mengandung: ")
        tampilkan("""
            SELECT p.kode_produk, p.nama_produk, s.nama AS supplier
            FROM produk AS p
            INNER JOIN supplier AS s ON p.supplier_id = s.id
            WHERE s.nama LIKE %s
        """, ("%" + kata + "%",))
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak tersedia.")

dbcursor.close()
konek.close()
print("Program selesai.")
