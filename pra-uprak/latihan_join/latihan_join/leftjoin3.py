from koneksi_swalayan import tampilkan

# Rekap belanja setiap pelanggan (pelanggan tanpa transaksi tetap tampil, total = 0)
sql = """
SELECT pl.nama,
       COUNT(pj.id) AS jumlah_transaksi,
       COALESCE(SUM(pj.total), 0) AS total_belanja
FROM pelanggan AS pl
LEFT JOIN penjualan AS pj
    ON pj.pelanggan_id = pl.id
GROUP BY pl.id, pl.nama
ORDER BY total_belanja DESC
"""

print("=== Rekap Belanja per Pelanggan ===")
tampilkan(sql)
