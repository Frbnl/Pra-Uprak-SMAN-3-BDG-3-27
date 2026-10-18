from koneksi_swalayan import tampilkan

# Pelanggan yang belum pernah melakukan transaksi
sql = """
SELECT pl.id, pl.nama, pl.telpon
FROM pelanggan AS pl
LEFT JOIN penjualan AS pj
    ON pj.pelanggan_id = pl.id
WHERE pj.id IS NULL
"""

print("=== Pelanggan yang belum pernah belanja ===")
tampilkan(sql)
