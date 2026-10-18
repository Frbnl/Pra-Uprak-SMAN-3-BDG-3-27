from koneksi_swalayan import tampilkan

# Tabel produk di KIRI, tabel supplier di KANAN
# RIGHT JOIN -> semua supplier tampil, walaupun belum punya produk
sql = """
SELECT s.id, s.nama AS nama_supplier,
       p.kode_produk, p.nama_produk
FROM produk AS p
RIGHT JOIN supplier AS s
    ON p.supplier_id = s.id
"""

print("=== RIGHT JOIN: Produk dan Supplier ===")
tampilkan(sql)
