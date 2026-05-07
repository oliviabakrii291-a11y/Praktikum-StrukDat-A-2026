'''
Soal 1. Fungsi Tambah Buku dengan Validasi

Topik: Fungsi, Parameter, Return Value, Dictionary | Estimasi waktu: 15 menit
Tuliskan jawaban kode Python Anda pada file: soal1.py (jangan ubah nama file)

Deskripsi:
Toko buku PyBook Store membutuhkan sebuah fungsi untuk menambahkan buku baru ke
dalam sistem. Fungsi ini harus memvalidasi data masukan sebelum menyimpannya.
Ketentuan Program:
1. Buat fungsi tambah_buku(nama, harga, stok) yang menerima tiga parameter:
nama buku (string), harga (int/float), dan stok (int).
2. Validasi input: harga harus lebih besar dari 0 dan stok tidak boleh bernilai negatif.
Jika tidak valid, cetak pesan error dan kembalikan nilai None.
3. Jika data valid, kembalikan sebuah dictionary dengan key: "nama", "harga", dan
"stok".
4. Di program utama, gunakan perulangan untuk meminta input data 3 buku dari
user, simpan ke dalam list, dan tampilkan seluruh isi list di akhir.

5. Program menampilkan daftar buku yang berhasil ditambahkan beserta seluruh
datanya di akhir eksekusi.
'''

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


print("\nDaftar Buku:")
for buku in daftar_buku:
    print(buku)
