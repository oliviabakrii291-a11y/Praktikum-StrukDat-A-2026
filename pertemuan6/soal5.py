'''
Deskripsi:
Gabungkan semua komponen dari soal 1 hingga 4 menjadi satu program lengkap PyBook
Store dengan menu interaktif berbasis teks. Pada soal ini, semua fungsi dan prosedur yang
telah dibuat di soal1.py hingga soal4.py ditulis ulang dan digabungkan dalam satu file
soal5.py.

Ketentuan Program:
Program menampilkan menu berikut dan berjalan dalam perulangan hingga user memilih

menu 5:
=== PyBook Store ===
1. Tambah Buku
2. Tampilkan Semua Buku
3. Beli Buku
4. Laporan Penjualan
5. Keluar
1. Menu 1 - Tambah Buku: Gunakan fungsi tambah_buku() dan simpan hasilnya ke
dalam list katalog.
2. Menu 2 - Tampilkan Semua Buku: Tampilkan seluruh isi katalog dalam format
tabel yang rapi menggunakan f-string.
3. Menu 3 - Beli Buku: Gunakan prosedur proses_transaksi(). Simpan setiap
transaksi berhasil sebagai tuple (nama_buku, jumlah, total) ke list log_transaksi.

4. Menu 4 - Laporan Penjualan: Iterasi log_transaksi, tampilkan total pemasukan
keseluruhan dan buku terlaris menggunakan dictionary untuk menghitung
frekuensi.
5. Menu 5 - Keluar: Hentikan program dengan menampilkan pesan perpisahan
kepada user.
'''

print("=== PyBook Store ===")
print("1. Tambah Buku")


def tambah_buku(nama, harga, stok):

    while harga <= 0 and stok <= 0:
        print("Error! THarga dan stok buku tidak memenuhi persyaratan!")
        return None
    

    buku = {
             "nama": nama,
             "harga":harga,
             "stok":stok
            }
    
    return buku


daftar_buku = []


for i in range(3):

    print("Input buku ke-: ", i+1)
    nama = str(input("Nama Buku: "))
    harga = int(input("Harga Buku: "))
    stok = int(input("Stok Buku: "))

    data = tambah_buku(nama, harga, stok)


    if data != None:
        daftar_buku.append(data)


print("2. Tampilkan Semua Buku")
print("\nDaftar Buku:")
for buku in daftar_buku:
    print(buku)


print("3. Beli Buku")

print("4. Laporan Penjualan")


print("5. Keluar")