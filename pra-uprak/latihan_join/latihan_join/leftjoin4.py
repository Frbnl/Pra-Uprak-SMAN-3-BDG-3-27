from koneksi_swalayan import tampilkan

# Penjualan yang belum memiliki data pembayaran
sql = """
SELECT pj.id, pj.tanggal, pj.total
FROM penjualan AS pj
LEFT JOIN pembayaran AS pb
    ON pb.penjualan_id = pj.id
WHERE pb.id IS NULL
"""

print("=== Penjualan yang belum dibayar ===")
tampilkan(sql)
