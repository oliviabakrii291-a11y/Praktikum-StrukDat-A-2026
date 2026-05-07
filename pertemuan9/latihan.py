'''
Soal Struktur Data Pertemuan 9

Bagian A — Double Linked List
Sistem daftar buku toko "Literasi"
Toko buku "Literasi" ingin mencatat daftar buku (judul & pengarang)
menggunakan Double Linked List agar bisa ditelusuri dari depan maupun belakang.
1. Buat class Node dengan atribut judul, pengarang, prev, dan next.
2. Buat fungsi insert_tail(), lalu tambahkan buku: Laskar Pelangi, Bumi Manusia,
dan Sang Pemimpi.
3. Buat fungsi print_forward() dan print_backward(), lalu jalankan keduanya.
4. Buat fungsi delete_by_judul(), hapus buku "Bumi Manusia", lalu tampilkan list
kembali.
'''


class Node:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.prev = None
        self.next = None



class DoublyLinkedList:
    def __init__(self):
        self.head = None

      # Menambah node di akhir
    def insert_tail(self, judul):
        new_node = Node(judul, None)  

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            return

        # Cari node terakhir
        current = self.head
        while current.next:
            current = current.next

        # Hubungkan node terakhir dengan node baru
        current.next = new_node
        new_node.prev = current



     # Menampilkan dari depan ke belakang
    def display_forward(self):
        current = self.head
        while current:
            print(current.judul, end=" <-> ")
            current = current.next
        print("None")

    # Menampilkan dari belakang ke depan
    def display_backward(self):
        current = self.head

        # Pergi ke node terakhir
        while current and current.next:
            current = current.next

        # Tampilkan mundur
        while current:
            print(current.judul, end=" <-> ")
            current = current.prev
        print("None")



    # Menghapus node berdasarkan judul
    def delete_by_judul(self, judul):   
        current = self.head

        while current:
            if current.judul == judul:
                # Jika node pertama
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                  # Menghubungkan node sebelumnya dengan node berikutnya
                    current.prev.next = current.next

                    if current.next:
                      # Menghubungkan node berikutnya dengan node sebelumnya
                        current.next.prev = current.prev
                return

            current = current.next




literasi = DoublyLinkedList()
literasi.insert_tail("Laskar Pelangi")
literasi.insert_tail("Bumi Manusia")
literasi.insert_tail("Sang Pemimpi")
print("Forward:")
literasi.display_forward()

print("Backward:")
literasi.display_backward()

literasi.delete_by_judul("Bumi Manusia")

print("Setelah hapus Bumi Manusia:")
literasi.display_forward()




'''
Bagian B — Circular Linked List
Sistem antrian kasir toko "Literasi"
Kasir toko menggunakan Circular Linked List untuk antrian pelanggan. Antrian
awal: Andi → Budi → Citra → Dina → (kembali ke Andi).
1. Buat class Node dengan atribut nama dan next. Buat fungsi insert_tail() dan
tambahkan 4 pelanggan.
2. Buat fungsi print_antrian() untuk menampilkan satu putaran antrian.
3. Tambahkan pelanggan baru Edo di akhir antrian menggunakan insert_tail(), lalu
tampilkan antrian.
4. Buat fungsi delete_head(), hapus Andi (sudah dilayani), lalu tampilkan antrian.
'''

    
class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Menambah node di akhir
    def insert_tail(self, nama):
        new_node = Node(nama)

        # Jika linked list kosong
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Sambungkan node terakhir ke node baru
        current.next = new_node
        new_node.next = self.head



    # Menampilkan linked list
    def display(self):
        if self.head is None:
            print("Linked list kosong")
            return

        current = self.head

        while True:
            print(current.nama, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(kembali ke head)")


    def delete_head(self, nama):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            return

        current = self.head

        # Cari node terakhir
        while current.next != self.head:
            current = current.next

        # Node terakhir menunjuk ke head berikutnya
        current.next = self.head.next

        # Pindahkan head
        self.head = self.head.next


print("\n")

antrian = CircularLinkedList()
antrian.insert_tail("Andi") 
antrian.insert_tail("Budi")
antrian.insert_tail("Citra")
antrian.insert_tail("Dina")

print("Antrian awal:")
antrian.display()
        
antrian.insert_tail("Edo")
print("Setelah tambah Edo:")
antrian.display()

antrian.delete_head("Andi")
print("Setelah hapus Andi:")    
antrian.display()   

    