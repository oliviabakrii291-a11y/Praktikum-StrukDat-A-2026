print("Sistem Penyimpanan Data Buku Perpustakaan\n")

'''
Sebuah perpustakaan ingin membuat sistem sederhana untuk menyimpan data
buku menggunakan hash table.
Setiap buku disimpan dalam format:
kode_buku : judul_buku
Contoh:
BK222 : Python Dasar
'''


#SISTEM MENYIMPAN DATA PERPUSTAKAAN
class HashTable_Perpus:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    

    def hash_func(self, kode):
        # Rumus: jumlah Unicode karakter % panjang bucket
        total_unic = 0
        for char in str(kode):
            total_unic += ord(char)
        return total_unic % self.size


    #untuk menambahkan buku baru, update buku jika kode sudah ada
    def insert_buku(self, kode, judul):
        index_bucket = self.hash_func(kode)
        bucket = self.table[index_bucket]

        #cek buku jika sudah ada untuk di update
        for i, (k, j) in enumerate(bucket):
            if k == kode: #jika ditemukan
                bucket[i] = (kode, judul)
                print(f"Data dengan kode '{kode}' berhasil di update")
                return
        #jika belum ada, tambah buku baru
        bucket.append((kode, judul))
        print(f"Data '{kode}' : '{judul}' berhasil ditambahkan!")


    #untuk menampilkan buku berdasarkan kode
    def search_buku(self, kode):
        index_bucket = self.hash_func(kode)
        bucket = self.table[index_bucket]

        #cari berdasarkan kode di bucket
        for k, j in bucket: 
            if k == kode:
                return j
        return "Buku tidak ditemukan" #jika tidak ditemukan 
    

    #menghapus berdasarkan kode
    def delete_buku(self, kode):
        index_bucket = self.hash_func(kode)
        bucket = self.table[index_bucket]

        #cari posisi data
        for i, (k, j) in enumerate(bucket):
            if k == kode:
                del bucket[i] #hapus data jika ditemukan
                print(f"Data dengan kode '{kode}' berhasil dihapus!")
                return True
        print(f"Kode '{kode}' tidak ditemukand didata") #jika kode tidak ditemukan
        return False


    #untuk menampilkan isi hash table
    def display_buku(self):
        
        print("================= PENYIMPANAN BUKU DI PERPUSTAKAAN =================")

        
        for kode, judul in enumerate(self.table, 1):
            print(f"'{kode}' : '{judul}'")
            
        print("====================================================================")

#--- program utama ---#
buku = HashTable_Perpus()

#insert data buku
print("\nInsert Data Buku: ")
buku.insert_buku("BK111", "Mahir C++ Dalam Satu Jam")
buku.insert_buku("BK222", "Python Dasar")
buku.insert_buku("BK333", "Matematika Diskrit")
buku.insert_buku("BK444", "Atomic Habits")
buku.insert_buku("BK555", "Pemrograman Berorientasi Objek")
buku.insert_buku("BK666", "Algoritma dan Struktur Data")
buku.insert_buku("BK777", "Belajar Data Science")
buku.insert_buku("BK888", "cybersecurity untuk Pemula")
buku.insert_buku("BK999", "Machine Learning dengan Python")

#tampilkan buku yang sudah disimpan
print("\nDisplay Buku Saat Ini: ")
buku.display_buku()

#insert buku baru 
print("\nInsert Data Buku: ")
buku.insert_buku("BK045", "Mein Kampf")
buku.insert_buku("BK111", "Bumi Manusia")

#tampilkan buku yang sudah disimpan
print("\nDisplay Buku Saat Ini: ")
buku.display_buku()

#cari buku 
print("\nCari Buku: ")
print("Masukkan kode buku:", buku.search_buku("BK999")) #cari buku berdasarkan kode yang ada dalam hash table
print("Masukkan kode buku:", buku.search_buku("BK505")) #cari buku yang tidak ada dalam hash table

#hapus buku
print("\nDelete Buku: ") 
buku.delete_buku("BK045") #hapus buku berdasarkan kode yang ada dalam hash table
buku.delete_buku("BK505") #hapus buku yang tidak ada dalam hash table

#tampilkan lagi buku yang sudah disimpan setelah dihapus
print("\nDisplay Buku Saat Ini: ") 
buku.display_buku()