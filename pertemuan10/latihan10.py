'''
Tugas Anda: Anda diminta untuk mengimplementasikan sistem ini menggunakan
dua cara yang berbeda:
1. Menggunakan List biasa (Dynamic Array) bawaan Python.
2. Menggunakan Linked List.

Kedua implementasi tersebut wajib memiliki 5 operasi dasar Stack berikut:
1. is_empty(): Memeriksa apakah riwayat kosong (mengembalikan True atau
False).
2. push(url): Menambahkan URL baru ke posisi teratas (pengguna membuka
halaman baru).
3. pop(): Menghapus dan mengembalikan URL di posisi teratas (pengguna
menekan tombol 'Back'). Jika kosong, kembalikan teks "Riwayat kosong".
4. peek(): Melihat URL yang ada di posisi teratas tanpa menghapusnya (melihat
halaman yang sedang aktif). Jika kosong, kembalikan None.
5. size(): Menghitung total URL yang tersimpan di dalam riwayat saat ini.
'''

print("Bagian 1: Implementasi Menggunakan List Biasa")

class StackList:

    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Riwayat Kosong"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)


# Buat Stack
print("\n")
myStack = StackList()

myStack.push('Satu Unri')
myStack.push('Netflix')
myStack.push('Instagram')

print("Stack: ", myStack.items)
print("Pop: ", myStack.pop())
print("Stack setelah Pop: ", myStack.items)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.is_empty())
print("Size: ", myStack.size())



print

print("Bagian 2: Implementasi Menggunakan Linked List")

class Node:

    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
           return self.size == 0

    def push(self, url):
        new_node = Node(url)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Riwayat kosong"
        url = self.top.url
        self.top = self.top.next
        self.count -= 1
        return url

    def peek(self):
        if self.is_empty():
            return "Stack Kosong"
        return self.top.url
    
    def size(self):
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")

            currentNode = currentNode.next
    print()

    
print("\n")

myStack2 = StackLinkedList()
myStack2.push('Google')
myStack2.push('Youtube')
myStack2.push('Mobilelengends')


print("LinkedList: ", end="")
myStack2.traverseAndPrint()
print("\nPeek: ", myStack2.peek())
print("Pop: ", myStack2.pop())
print("LinkedList after Pop: ", end="")
myStack2.traverseAndPrint()
print("\nisEmpty: ", myStack2.is_empty())
print("Size: ", myStack2.size())
