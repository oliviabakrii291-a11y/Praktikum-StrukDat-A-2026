
'''
2. Case: Kendaraan yang sudah selesai urusan harus keluar melalui satu pintu yang
sama. Karena ini antrean, kendaraan yang pertama datang harus pertama keluar
(FIFO). Namun, karena ada kendala teknis, terkadang ada kendaraan di urutan
tertentu yang "mogok" dan harus dihapus dari daftar antrean secara paksa.

a. Tugas:
1. Buat struktur Node dan LinkedList.
2. Buat fungsi tambahKendaraan(plat) untuk menambah
kendaraan ke akhir list (Tail).
3. Buat fungsi hapusKendaraan(plat) untuk menghapus kendaraan
tertentu jika ia mogok di tengah antrean.

b. Logika: Melakukan traversal (penelusuran) dari head hingga menemukan
plat yang cocok, lalu menyambungkan node sebelumnya langsung ke node
sesudahnya.
'''


class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def tambahKendaraan(self, plat):
        node_baru = Node(plat)

        if self.head is None:
            self.head = node_baru
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = node_baru

    def hapusKendaraan(self, plat):
        current = self.head
        prev = None

        while current:
            if current.plat == plat:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return

            prev = current
            current = current.next

    def tampilkan(self):
        current = self.head
        while current:
            print(current.plat, end=" -> ")
            current = current.next
        print("None")


parkir = LinkedList()

parkir.tambahKendaraan("B 1234 ABC")
parkir.tambahKendaraan("D 8888 XYZ")
parkir.tambahKendaraan("A 111 TUV")
parkir.tambahKendaraan("B 2022 EFG")

print("Antrean awal:")
parkir.tampilkan()

parkir.hapusKendaraan("A 111 TUV")

print("Setelah kendaraan mogok dihapus:")
parkir.tampilkan()