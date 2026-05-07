'''
Soal 2. Pencarian Buku dengan List of Dictionary
Topik: List of Dictionary, Manipulasi Collection | Estimasi waktu: 20 menit
Tuliskan jawaban kode Python Anda pada file: soal2.py (jangan ubah nama file)

Deskripsi:
PyBook Store memerlukan fitur pencarian buku agar pelanggan dapat menemukan buku
berdasarkan kata kunci tanpa mengetahui nama lengkapnya.

Ketentuan Program:
Gunakan data katalog berikut (dapat ditulis langsung di kode):
katalog = [
{'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
{'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
{'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]
1. Buat fungsi cari_buku(katalog, keyword) yang mencari buku berdasarkan
keyword, yaitu substring dari nama buku yang bersifat case-insensitive.
2. Fungsi mengembalikan list semua buku yang sesuai dengan keyword tersebut.
3. Jika tidak ada buku yang ditemukan, kembalikan list kosong dan tampilkan pesan:
"Buku tidak ditemukan."
4. Di program utama, minta user memasukkan keyword pencarian dan tampilkan
hasilnya dengan format yang rapi.
'''



def cari_buku(katalog, keyword):
    hasil_cari = []
    
    for buku in katalog:
        if keyword.lower() in buku['nama'].lower():
            hasil_cari.append(buku)
    
    if len(hasil_cari) == 0:
        print("Buku tidak ditemukan.")
    
    return hasil_cari



katalog = [
        {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
        {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
        {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
    ]



keyword_input = input("Masukkan keyword: ")
pencarian = cari_buku(katalog, keyword_input)


if pencarian:
    print(f"\nHasil pencarian untuk '{keyword_input}':")
    print("-" * 45)
    for b in pencarian:
        print(f"Nama: {b['nama']} | Harga: Rp{b['harga']} | Stok: {b['stok']}")
    print("-" * 45)


    



    

