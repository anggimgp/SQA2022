jam = int(input('Berapa jam kerja?: '))

if jam <= 40:
    gaji = 15000 * jam
else:
    gaji = 15000 * 40 + (jam-40) * 22500

print("Gaji anda", gaji)

pengeluaran = int(input("Pengeluaran anda?:"))
nabung = str(gaji - pengeluaran)
if gaji > pengeluaran:
    print('Anda bisa menabung. Besar tabungan anda sebesar Rp.', nabung)
elif gaji == pengeluaran:
    print('Anda tidak bisa menabung')
else:
    print('Cari tambahan')
