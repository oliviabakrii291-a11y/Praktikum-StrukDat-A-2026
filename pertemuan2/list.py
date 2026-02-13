#list / tempat menyimpan banyak data
my_cake = ["brownies", "cupcake", "donut"]
print(my_cake)


my_cake = ["brownies", "cupcake", "brownies", "donut"]
print(my_cake)


my_cake = ["brownies", "cupcake", "donut"]
print(len(my_cake))



my_cake = ["brownies", "cupcake", "donut"]
print(my_cake)
angka = [1, 2, 3, 4, 5]
print(angka)
list3 = [True, False, False]
print(list3)



my_list1 = ["abcd", 44, True, 5000, "haiii"]
print(my_list1)



my_cake = ["brownies", "cupcake", "donut"]
print(type(my_cake))



thislist = list(("brownies", "cupcake", "donut"))
print(thislist)


#access items
my_cake = ["brownies", "cupcake", "donut"]
print(my_cake[2])


#indeks negatif
my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
print(my_cake[2:5])



my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
print(my_cake[-2:-1])

 #change item
my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
my_cake[1] = "bolu kemojo"
print(my_cake)



my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
my_cake[1 : 3] = ["bolu kemojo", "kue putu"]
print(my_cake)


my_cake = ["brownies", "cupcake", "donut", "nastar", "lapis legit"]
my_cake.insert(2, "kue putu")
print(my_cake)

#nambah item ke list
my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_cake.append("nastar")
print(my_cake)

#insert
my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_cake.insert(2, "nastar")
print(my_cake)


my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_drink = ["boba", "mixue"]
my_cake.extend(my_drink)
print(my_cake)


my_cake = ["brownies", "cupcake", "donut", "lapis legit"]
my_cakeTuple = ["nastar", "bolu kemojo"]
my_cake.extend(my_cakeTuple)
print(my_cake)


#remove
thislist = ["ayam" , "kucing", "anjing"]
thislist.remove("anjing")
print(thislist)


thislist = ["ayam" , "kucing", "anjing"]
thislist.pop(1)
print(thislist)


thislist = ["ayam" , "kucing", "anjing"]
thislist.pop()
print(thislist)


thislist = ["ayam" , "kucing", "anjing"]
del thislist[0]
print(thislist)

#menghapus
'''
thislist = ["ayam" , "kucing", "anjing"]
del thislist 
print(thislist)
'''


thislist = ["ayam" , "kucing", "anjing"]
thislist.clear
print(thislist)


#for in list
thislist = ["ayam" , "kucing", "anjing"]
for x in thislist:
  print(x)


#loop through index
thislist = ["ayam", "kucing", "anjing"]
for i in range(len(thislist)):
  print(thislist[i])


#while loop
thislist = ["ayam", "kucing", "anjing", "musang", "kambing"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#list comprehension
thislist = ["ayam", "kucing", "anjing", "musang", "kambing"]
[print(x) for x in thislist]


animals = ["ayam", "kucing", "anjing", "musang", "kambing"]
newlist = []

for x in animals:
  if "a" in x:
    newlist.append(x)

print(newlist)


animals = ["ayam", "kucing", "anjing", "musang", "kambing"]

newlist = [x for x in animals if "a" in x]

print(newlist)

#condition
animals = ["ayam", "kucing", "anjing", "musang", "kambing"]

newlist = [x for x in animals if x != "musang"]

print(newlist)


#iterable
newlist = [x for x in range(8)]

print(newlist)

#expression
animals = ["ayam", "kucing", "anjing", "musang", "kambing"]
newlist = [x.upper() for x in animals]

print(newlist)

#sort
thislist = ["black", "red", "purple", "yellow", "white"]
thislist.sort()
print(thislist)


thislist = ["black", "red", "purple", "yellow", "white"]
thislist.sort(reverse = True)
print(thislist)


#costumize
def jarak_ke_10(n):
    return abs(n - 10)

angka = [3, 15, 8, 20, 11]
angka.sort(key=jarak_ke_10)
print(angka)

#case sensitive
thislist = ["Ayam", "kucing", "Sapi", "bebek"]
thislist.sort()
print(thislist)

#reverse
thislist = ["Ayam", "kucing", "Sapi", "bebek"]
thislist.reverse()
print(thislist)


#copy
my_cat = ["yoyo", "bams", "ciko",  "cemon", "milo"]
mylist = my_cat.copy()
print(mylist)

#list
my_cat = ["yoyo", "bams", "ciko",  "cemon", "milo"]
mylist = list(my_cat)
print(mylist)


#slice
my_cat = ["yoyo", "bams", "ciko",  "cemon", "milo"]
mylist = my_cat[:]
print(mylist)


#join
list1 = ["x", "y", "z"]
list2 = [7, 8, 9]

list3 = list1 + list2
print(list3)


list1 = ["x", "y", "z"]
list2 = [7, 8, 9]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["x", "y", "z"]
list2 = [7, 8, 9]
list1.extend(list2)
print(list1)
