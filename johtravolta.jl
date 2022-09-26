println("masukan jam kerja: ")
j = parse(Int64, readline())

if j >= 40
	gaji = 40 * 15000 + (j - 40) * 22500
else
	gaji = j * 15000
end
println("gaji anda: ", gaji)

println("Pengeluaran anda?:")
pengeluaran = parse(Int64, readline())

nabung = gaji - pengeluaran
if gaji > pengeluaran
    println("Anda bisa menabung. Besar tabungan anda sebesar Rp.", nabung)
else
    println("Anda tidak bisa menabung")
end