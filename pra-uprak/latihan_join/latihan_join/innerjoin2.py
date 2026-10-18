from koneksi_swalayan import tampilkan

# Penjualan + nama pelanggan, total di atas nilai tertentu
sql = """
SELECT pj.id, pj.tanggal, pl.nama AS nama_pelanggan,
       pj.keterangan, pj.total
FROM penjualan AS pj
INNER JOIN pelanggan AS pl
    ON pj.pelanggan_id = pl.id
WHERE pj.total > %s
ORDER BY pj.tanggal
"""

print("=== INNER JOIN: Penjualan dan Pelanggan ===")
tampilkan(sql, (100000,))
