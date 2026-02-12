#list / tempat menyimpan banyak data
'''
my_cake = ["brownies", "cupcake", "donut"]
print(my_cake)
'''
'''
my_cake = ["brownies", "cupcake", "brownies", "donut"]
print(my_cake)
'''

'''
my_cake = ["brownies", "cupcake", "donut"]
print(len(my_cake))
'''

'''
my_cake = ["brownies", "cupcake", "donut"]
print(my_cake)
angka = [1, 2, 3, 4, 5]
print(angka)
list3 = [True, False, False]
print(list3)
'''
'''

my_list1 = ["abcd", 44, True, 5000, "haiii"]
print(my_list1)
'''

'''
my_cake = ["brownies", "cupcake", "donut"]
print(type(my_cake))
'''


'''
thislist = list(("brownies", "cupcake", "donut"))
print(thislist)
'''

#access items
'''
my_cake = ["brownies", "cupcake", "donut"]
print(my_cake[2])
'''

#indeks negatif
'''
my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
print(my_cake[2:5])
'''

'''
my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
print(my_cake[-2:-1])
'''
 #change item

'''
my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
my_cake[1] = "bolu kemojo"
print(my_cake)
'''

'''
my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
my_cake[1 : 3] = ["bolu kemojo", "kue putu"]
print(my_cake)
'''

'''
my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
my_cake.insert(2, "kue putu")
print(my_cake)
'''
#nambah item ke list
'''
my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_cake.append("nastar")
print(my_cake)
'''
#insert
'''
my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_cake.insert(2, "nastar")
print(my_cake)
'''
'''
my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_drink = ["boba", "mixue"]
my_cake.extend(my_drink)
print(my_cake)
'''
'''
my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_cakeTuple = ["nastar", "bolu kemojo"]
my_cake.extend(my_cakeTuple)
print(my_cake)
'''

#remove
'''
thislist = ["ayam" , "kucing", "anjing"]
thislist.remove("anjing")
print(thislist)
'''
'''
thislist = ["ayam" , "kucing", "anjing"]
thislist.pop(1)
print(thislist)
'''
'''
thislist = ["ayam" , "kucing", "anjing"]
thislist.pop()
print(thislist)
'''
'''
thislist = ["ayam" , "kucing", "anjing"]
del thislist[0]
print(thislist)
'''

'''
thislist = ["ayam" , "kucing", "anjing"]
del thislist
print(thislist)
'''

thislist = ["ayam" , "kucing", "anjing"]
thislist.clear()
print(thislist)

