
class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree: 
    def __init__ (self):
        self.root = None

    def insert(self, data):
        #langkah 1
        new = Node(data)

        #Langkah 2
        if self.root is None:
            #jika iya
            self.root = new
            return

        #Langkah 3
        P = self.root
        Q = self.root

        #Langkah 4
        while Q is not None and new.data!= P.data :
            #Langkah 5
            P = Q

            #Langkah 6
            if new.data < P.data:
                Q = P.left
            else:
                Q = P.right

        #Langkah 7
        if new.data == P.data:
            #jika iya
            print("Data Duplikat")

        #Langkah 8
        if new.data < P.data:
            #jika iya
            P.left = new
        #jika tidak
        else:
            P.right = new


bst = BinarySearchTree()

bst.insert(1)
bst.insert(22)
bst.insert(33)
bst.insert(69)
bst.insert(98)


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" -> ")
        inorder(node.right)

inorder(bst.root)





class BinaryTree:

    #implementasi binary tree
    def __init__ (self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)


    #memasukkan child kiri dari suatu node
    def insert_left (self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node


    #memasukkan child kanan dari suatu node
    def insert_right (self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node


def preorder(node):
    if node is not None:
        print(node.data, end= " - > ")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" -> ")
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end= " - > ")

tree = BinaryTree()

tree.insert_root("F")
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "G")
tree.insert_left(tree.root.left, "A")
tree.insert_right(tree.root.left, "D")
tree.insert_right(tree.root.left.right, "C")
tree.insert_right(tree.root.left.right, "E")
tree.insert_right(tree.root.right, "I")
tree.insert_right(tree.root.right.right, "H")

print("Preorder : ", end=" ")
preorder(tree.root)
print()
print("Inoorder : ", end=" ")
inorder(tree.root)
print()
print("Postorder : ", end=" ")
postorder(tree.root)




