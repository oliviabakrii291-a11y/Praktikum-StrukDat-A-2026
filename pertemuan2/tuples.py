#tuples
thistuple = ("kucing", "anjing", "sapi", "kambing")
print(thistuple)


#allow duplicat
thistuple = ("kucing", "anjing", "sapi", "anjing", "kambing")
print(thistuple)


#len()
thistuple = ("kucing", "anjing", "sapi", "anjing", "kambing")
print(len(thistuple))


#buat tuple dgn 1 itemm
thistuple = ("cherry",)
print(type(thistuple))

#bukan tuple
thistuple = ("cherry")
print(type(thistuple))


#mengakses tuple
thistuple = ("kucing", "anjing", "sapi", "kambing")
print(thistuple[2])

#negatif index
thistuple = ("kucing", "anjing", "sapi", "kambing")
print(thistuple[-3])


#menentukan rentang index
thistuple = ("kucing", "anjing", "sapi", "kambing")
print(thistuple[1:2])


#menentukan rentang index negatif
thistuple = ("kucing", "anjing", "sapi", "kambing")
print(thistuple[-2:-1])


#check if item exist
thistuple = ("kucing", "anjing", "sapi", "kambing")
if "anjing" in thistuple:
    print("Yes, 'anjing' is in the animals tuple")


#mengubah nilai tuple
x = ("kucing", "anjing", "sapi", "kambing")
y = list(x)
y[1] = "panda"
x = tuple(y)

print(x)


#konversi
thistuple = ("kucing", "anjing", "sapi", "kambing")
y = list(thistuple)
y.append("jerapah")
thistuple = tuple(y)

print(thistuple)


#menambahkan tuple + tuple
thistuple = ("kucing", "anjing", "sapi", "kambing")
y = ("ayam",)
thistuple += y

print(thistuple)


#remove
thistuple = ("kucing", "anjing", "sapi", "kambing")
y = list(thistuple)
y.remove("sapi")
thistuple = tuple(y)

print(thistuple)


#del()
thistuple = ("kucing", "anjing", "sapi", "kambing")
del thistuple
print(thistuple)


#packing tuples
cakes = ("brownies", "nastar", "lapis legit")
print(cakes)


#unpacking
cakes = ("brownies", "nastar", "lapis legit")

(green, yellow, red) = cakes

print(green)
print(yellow)
print(red)


# *
cakes = ("brownies", "nastar", "lapis legit")
(green, yellow, *red) = cakes

print(green)
print(yellow)
print(red)


cakes = ("brownies", "nastar", "lapis legit")
(green, *tropic, red) = cakes

print(green)
print(tropic)
print(red)


#loop
cakes = ("brownies", "nastar", "lapis legit")
for x in cakes:
    print(x)


#berdasarkan indeks
cakes = ("brownies", "nastar", "lapis legit")
for i in range(len(cakes)):
  print(cakes[i])


#while
cakes = ("brownies", "nastar", "lapis legit")
i = 0
while i < len(cakes):
  print(cakes[i])
  i = i + 1

#gabungkan tuple
tuple1 = ("abc", "bcd" , "cde")
tuple2 = (5, 6, 7)

tuple3 = tuple1 + tuple2
print(tuple3)

#multiple tuples
animals = ("sapi", "ayam", "kambing")
mytuple = animals * 2

print(mytuple)