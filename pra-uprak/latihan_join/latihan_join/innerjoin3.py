from koneksi_swalayan import tampilkan

# Nota penjualan lengkap: menggabungkan 4 tabel sekaligus
sql = """
SELECT pj.id AS no_nota, pj.tanggal, pl.nama AS pelanggan,
       p.nama_produk, pd.kuantitas, pd.total
FROM penjualan_detail AS pd
INNER JOIN penjualan AS pj
    ON pd.penjualan_id = pj.id
INNER JOIN pelanggan AS pl
    ON pj.pelanggan_id = pl.id
INNER JOIN produk AS p
    ON pd.produk_id = p.id
ORDER BY pj.id
"""

print("=== INNER JOIN 4 tabel: Nota Penjualan Lengkap ===")
tampilkan(sql)
