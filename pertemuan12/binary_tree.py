
'''
Tugas
Buatlah program Python untuk membangun struktur Binary Tree secara manual dan melakukan
ketiga jenis traversal tersebut.
Operasi yang Wajib Diimplementasikan
1. insert_manual(): Membangun pohon sesuai struktur yang ditentukan di skenario.
2. traverse_preorder(): Menampilkan urutan gudang dengan metode Pre-Order.
3. traverse_inorder(): Menampilkan urutan gudang dengan metode In-Order.
4. traverse_postorder(): Menampilkan urutan gudang dengan metode Post-Order.
5. get_leaf_nodes(): Menampilkan daftar gudang yang merupakan Leaf Node (gudang ujung
yang tidak punya cabang lagi).
'''


print("Struktur Data : Binary Tree\n")

#class untuk node

class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None


#class binary tree 
class BinaryTree:
    def __init__(self):
        self.root = None
    
    #insert manual : Membangun pohon sesuai struktur yang ditentukan di skenario.
    def insert_root(self, data):
        self.root = Node(data)

    #insert ke kiri
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
            #kalau node udah ada,  node lama bakal digeser ke bawah
            #terus node baru masuk di atasnya
    
    #insert ke kanan
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node
            #sama kayak insert left, tapi ini buat kanan
            


#Menampilkan urutan gudang dengan metode Pre-Order.
def traverse_preorder(node):
    if node is None:
        return
    print(node.data, end=" - ") #kunjungi node dulu
    traverse_preorder(node.left) #lalu ke kiri
    traverse_preorder(node.right) #baru ke kanan


#Menampilkan urutan gudang dengan metode In-Order.
def traverse_inorder(node):
    if node is None:
        return
    traverse_inorder(node.left) #ke kiri dulu
    print(node.data, end=" - ") #baru kunjungi node
    traverse_inorder(node.right) #lalu ke kanan


#Menampilkan urutan gudang dengan metode Post-Order.
def traverse_postorder(node):
    if node is None:
        return
    traverse_postorder(node.left) #ke kiri dulu
    traverse_postorder(node.right) #lalu ke kanan
    print(node.data, end=" - ") #baru kunjungi node

#Menampilkan daftar gudang yang merupakan Leaf Node (gudang ujung yang tidak punya cabang lagi).
def get_leaf_nodes(node):
    if node is None: #kalau node kosong, return list kosong
        return []
    if node.left is None and node.right is None: #kalau ini leaf node, return list dengan data node ini
        return [node.data]
    
    return get_leaf_nodes(node.left) + get_leaf_nodes(node.right) 
    #gabungkan hasil leaf dari kiri dan kanan
    
#MAIN PROGRAM
pohon_ = BinaryTree()

#skenario pengujian
pohon_.insert_root("A")  #root
pohon_.insert_left(pohon_.root, "B")  #B di kiri A
pohon_.insert_left(pohon_.root.left, "D")  #D di kiri
pohon_.insert_right(pohon_.root.left, "E")  #E di kanan B
pohon_.insert_right(pohon_.root, "C")  #C di kanan A
pohon_.insert_right(pohon_.root.right, "F")  #F di kanan C

#tampilan

print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("======================================")
print("[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur berhasil dibuat.")

print("\nHASIL AUDIT:")
print("1. Pre-Order : ", end="")
traverse_preorder(pohon_.root)
print("\n2. In-Order : ", end="")
traverse_inorder(pohon_.root)
print("\n3. Post-Order : ", end="")
traverse_postorder(pohon_.root)
print("\n")
print(f"[DATA] Gudang Ujung (Leaf Nodes): {get_leaf_nodes(pohon_.root)}")
print("======================================")
print("Audit Selesai!")


