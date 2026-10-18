from koneksi_swalayan import tampilkan

# Semua supplier, termasuk yang belum punya produk
sql = """
SELECT s.id, s.nama AS nama_supplier,
       p.kode_produk, p.nama_produk
FROM supplier AS s
LEFT JOIN produk AS p
    ON p.supplier_id = s.id
"""

print("=== LEFT JOIN: Supplier dan Produk ===")
tampilkan(sql)
