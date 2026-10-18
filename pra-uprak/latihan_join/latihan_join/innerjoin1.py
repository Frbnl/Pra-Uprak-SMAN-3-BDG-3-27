from koneksi_swalayan import tampilkan

sql = """
SELECT p.id, p.kode_produk, p.nama_produk, p.harga, p.stok,
       s.nama AS nama_supplier
FROM produk AS p
INNER JOIN supplier AS s
    ON p.supplier_id = s.id"""

print("=== INNER JOIN: Produk dan Supplier ===")
tampilkan(sql)
