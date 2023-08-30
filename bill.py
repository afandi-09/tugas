# 1
print("=" * 30)
print("       Idris Market    ")
print("=" * 30)
# progres input user
harga = eval(input("Masukan Harga Barang : RP. "))
jumlah = eval(input("masukan jumlah barang : "))
# proses output
print()
total = harga *jumlah
print("Total Harga = ", "Rp",Total)
print()

bayar = eval(input("Masukan Jumlah Uang : Rp."))
kembalian = (bayar - total)
print("Uang Kembalian = ","Rp.",Kembalian)
print()