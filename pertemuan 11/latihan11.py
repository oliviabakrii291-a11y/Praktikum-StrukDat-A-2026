'''
Setiap pasien yang datang akan mendaftar dan masuk ke antrian. Dokter akan
memanggil pasien dari urutan paling pertama. Pak Hendra juga sering diminta
untuk:
Mengecek siapa pasien berikutnya yang akan dipanggil
Menghitung berapa banyak pasien yang masih menunggu
Mengecek apakah antrian sudah kosong
Mengosongkan antrian jika sesi poliklinik selesai

Karena mahasiswi magang bernama Sari baru saja belajar Python, ia diminta
untuk membuat program simulasi sistem antrian ini menggunakan Linked List
manual (bukan menggunakan list bawaan Python).
'''
'''
Skenario Pengujian
Program kamu harus dapat mensimulasikan kejadian berikut secara berurutan:
Skenario Pagi Hari — Poli Umum Sehat Bersama
1. Cek apakah antrian kosong (sebelum ada pasien)
2. Pasien BUDI mendaftar dengan keluhan "demam tinggi"
3. Pasien ANI mendaftar dengan keluhan "batuk pilek"
4. Pasien CITRA mendaftar dengan keluhan "sakit kepala"
5. Tampilkan jumlah pasien yang menunggu
6. Cek siapa pasien yang akan dipanggil berikutnya (peek)
7. Dokter memanggil pasien pertama (dequeue)
8. Pasien DODI mendaftar dengan keluhan "nyeri perut"
9. Tampilkan antrian saat ini (semua pasien)
10. Dokter memanggil pasien berikutnya (dequeue)
11. Tampilkan jumlah pasien yang masih menunggu
12. Sesi poliklinik selesai — kosongkan antrian (clear)
13. Cek apakah antrian sudah kosong
'''

'''
Petunjuk 1 — Struktur Node
Setiap pasien direpresentasikan sebagai sebuah Node yang menyimpan:
Data pasien (nama & keluhan)
Pointer ke pasien berikutnya

Latihan Praktikum 11 - Struktur Data 2

Node:
- nama
- keluhan
- next → Node berikutnya
'''



  # Node (Pasien)
class Node:
    def __init__(self, nama, keluhan):
        self.nama_pasien = nama
        self.keluhan_pasien = keluhan
        self.next = None

# Queue menggunakan Linked List
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # 1. Enqueue   (nambah pasien)
    def enqueue(self, nama, keluhan):
        pasien_baru = Node(nama, keluhan)

        if self.is_empty():
            self.head = self.tail = pasien_baru
        else:
            self.tail.next = pasien_baru
            self.tail = pasien_baru

        self._size += 1
        print(f"[DAFTAR] {nama} terdaftar dengan keluhan: {keluhan} (No. Antrian: {self._size})")

    # 2. Dequeue  (panggil pasien pertama)
    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return None

        keluar = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {keluar.nama_pasien} (keluhan: {keluar.keluhan_pasien})")
        return keluar

    # 3. Peek / Front (lihat pasien berikutnya)
    def peek(self):
        if self.is_empty():
            print("[PEEK] Antrian kosong!")
        else:
            print(f"[PEEK] Pasien berikutnya: {self.head.nama_pasien.upper()} — {self.head.keluhan_pasien}")

    # 4. Is Empty (cek apakah kosong)
    def is_empty(self):
        return self._size == 0

    # 5. Size   (hitung jumlah pasien)
    def size(self):
        return self._size

    # 6. Clear  (kosongkan antrian)
    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    # Tambahan: Tampilkan semua pasien dalam antrian
    def display(self):
        if self.is_empty():
            print("[ANTRIAN] Kosong")
            return

        print("\n[ANTRIAN SAAT INI]")
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.nama_pasien.upper()} → {current.keluhan_pasien}")
            current = current.next
            i += 1



# SIMULASI SESUAI SOAL
print("====================================")
print(" SISTEM ANTRIAN POLI UMUM")
print(" RS Sehat Bersama")
print("====================================\n")

antrian = Queue()

print("[CEK] Apakah antrian kosong?", "→ YA, antrian masih kosong." if antrian.is_empty() else "→ TIDAK")
antrian.enqueue("Budi", "demam tinggi")
antrian.enqueue("Ani", "batuk pilek")
antrian.enqueue("Citra", "sakit kepala")
print(f"\n[INFO] Jumlah pasien menunggu: {antrian.size()} orang")
antrian.peek()
antrian.dequeue()
antrian.enqueue("Dodi", "nyeri perut")
antrian.display()
antrian.dequeue()
print(f"\n[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")
antrian.clear()
print("[CEK] Apakah antrian kosong?", "→ YA, antrian sudah kosong." if antrian.is_empty() else "→ TIDAK")
print("\n")
print("\n====================================")
print(" Simulasi Selesai!")
print("====================================")