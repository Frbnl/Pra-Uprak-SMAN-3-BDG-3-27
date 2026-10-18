from koneksi_swalayan import tampilkan

# Penjualan yang belum dibayar, ditulis dengan RIGHT JOIN
# (hasilnya sama dengan LEFT JOIN pada leftjoin4.py, hanya urutan tabel dibalik)
sql = """
SELECT pj.id, pj.tanggal, pj.total
FROM pembayaran AS pb
RIGHT JOIN penjualan AS pj
    ON pb.penjualan_id = pj.id
WHERE pb.id IS NULL
"""

print("=== RIGHT JOIN: Penjualan yang belum dibayar ===")
tampilkan(sql)
