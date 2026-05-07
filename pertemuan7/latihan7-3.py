'''
3. Case: Layanan Valet VIP tetap memungkinkan kendaraan untuk menyalip.
Namun, karena keterbatasan sistem (Singly Linked List), petugas hanya bisa
melihat kendaraan di depannya. Kendaraan VIP baru dapat disisipkan tepat di
belakang kendaraan VIP tertentu yang sudah ada dalam antrean. Karena hanya
satu arah, untuk pengecekan urutan, petugas harus membacanya dari kendaraan
paling depan hingga paling belakang.

a. Tugas:
1. Gunakan struktur Singly Linked List (hanya memiliki pointer next).
2. Buat fungsi sisipkan_vip(plat_baru, plat_target):
Mencari plat_target dalam antrean, lalu menyisipkan
plat_baru tepat setelahnya.
3. Buat fungsi tampilkan_antrean() untuk menunjukkan urutan
kendaraan dari depan ke belakang.
b. Logika: Menelusuri list dari head untuk mencari plat_target. Setelah
ditemukan, buat node baru, hubungkan next dari node baru ke next milik
target, lalu ubah next milik target ke node baru.
'''


class Node:
  def __init__(self, plat_target, next):
    self.plat_target = plat_target
    self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def sisipkan_vip(plat_baru, plat_target):
       

    def tampilkan_antrean():
    