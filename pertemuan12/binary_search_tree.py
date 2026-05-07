
'''
Buatlah program Python yang mensimulasikan sistem katalog perpustakaan menggunakan Binary
Search Tree (BST). Program harus dibangun secara manual menggunakan class Node dan tidak
boleh menggunakan list/dictionary bawaan Python untuk menyimpan hierarki tree.
Operasi yang Wajib Diimplementasikan
1. insert(id_buku, judul): Menambahkan buku baru ke dalam BST sesuai aturan ID (Kiri <
Parent < Kanan).
2. search(id_buku): Mencari apakah suatu buku ada di katalog berdasarkan ID-nya.
3. traversal_inorder(): Menampilkan semua koleksi buku secara urut dari ID terkecil ke
terbesar.
4. get_min() & get_max(): Menemukan buku dengan ID terkecil dan terbesar.
5. height(): Menghitung total ketinggian (height) dari tree yang terbentuk.
'''

print("Struktur Data : Binary Search Tree (BST)\n")


class Node:
    def __init__(self, data, judul):
        self.data= data
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, data, judul):
        # 1. Buat node baru (new)
        new = Node(data, judul)

        # 2. Cek apakah root = None
        if self.root is None:
            self.root = new
            print(f"[INSERT] BERHASIL MEMASUKKAN : ID {data} - {judul}")
            return
        
        # 3. Tentukan P = root, Q = root
        P = self.root
        Q = self.root

        # 4. Kerjakan langkah 5 & 6 selama Q != None dan new.id != P.id
        while Q is not None and new.data != P.data:
            P = Q # 5. Tentukan P = Q

            # 6. Jika new < P -> Q ke kiri, jika tidak -> Q ke kanan
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        #7. Cek apakah new.info = P.info (Duplikat)
        if new.data == P.data:
            print("datanya duplikat")
            return

        #8. Jika new < P -> P.kiri = new, jika tidak -> P.kanan = new
        if new.data < P.data:
            P.left = new

        else:
            P.right = new

        print(f"[INSERT] BERHASIL MEMASUKKAN : ID {data} - {judul}")


    #Mencari apakah suatu buku ada di katalog berdasarkan ID-nya.
    def search (self, data):
        Searching_ = self.root
        while Searching_ is not None:
            if data == Searching_.data:
                return Searching_
            
            if data < Searching_.data:
                Searching_ = Searching_.left

            else:
                Searching_ = Searching_.right
        return None
    

    #Menampilkan semua koleksi buku secara urut dari ID terkecil ke terbesar.
    def traversal_inorder(self, node): 
        if node is not None:
            self.traversal_inorder(node.left)
            print(node.data, "-", node.judul)
            self.traversal_inorder(node.right)


    #Menemukan buku dengan ID terkecil dan terbesar.
    def get_min(self):
            if self.root is None:
                return None
            
            Min_ = self.root
            while Min_.left is not None:
                Min_ = Min_.left
            return Min_.data
        
    def get_max(self):
        Max_ = self.root
        while Max_.right is not None:
            Max_ = Max_.right
        return Max_.data
    
    #Menghitung total ketinggian (height) dari tree yang terbentuk.
    def height(self, node):
        if node is None:
            return -1
        left_hight = self.height(node.left)
        right_hight = self.height(node.right)

        if left_hight > right_hight:
            return left_hight + 1
        else:
            return right_hight +1
        



bst_data = BinarySearchTree()

print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=======================================================")

#Input Data: Masukkan buku-buku berikut secara berurutan:
bst_data.insert(50, "Dasar Pemograman")
bst_data.insert(30, "Struktur Data")
bst_data.insert(70, "Kecerdasan Buatan")
bst_data.insert(20, "Matematika Diskrit")
bst_data.insert(40, "Basis Data")
bst_data.insert(60, "Jaringan Komputer")
bst_data.insert(80, "Sistem Operasi")


print("\n\n[INFO] Koleksi Buku (In-Order Traversal):", end= " ")
bst_data.traversal_inorder(bst_data.root)

#Cek Koleksi
bst_data.traversal_inorder(bst_data.root)

#Pencarian
hasil = bst_data.search(60)
print("\n")

if hasil:
    print(f"[SEARCH] Mencari ID 60... Ditemukan! Judul: {hasil.judul}")
else:
    print(f"[SEARCH] Mencari ID 60... Data tidak ditemukan.")

hasil = bst_data.search(100)
if hasil:
    print(f"[SEARCH] Mencari ID 100... Ditemukan! Judul: {hasil.judul}")
else:
    print(f"[SEARCH] Mencari ID 100... Data tidak ditemukan.")  


#statistik
print(f"\n[STATISTIK] ID TERKECIL: ",bst_data.get_min())
print(f"[STATISTIK] ID TERBESAR: ",bst_data.get_max())

#analisis struktur
Tinggi = bst_data.height(bst_data.root)

print(f"[INFO] Tinggi (Height) Tree: {Tinggi}")
print("=========================================")
print("Simulasi selesai!")