#ada tiga tipe data numerik di Python
#int = bilangan bulat, postif dan negatif, tanpa desimal, tanpa koma
'''
a = 10
b = -10
c = 0   
print(type(a))
print(type(b))
print(type(c))
'''

#float = bilangan desimal, postif dan negatif, dengan koma
'''
x = 2.20
y = 2.0
z = -25.25
print(type(x))
print(type(y))
print(type(z))
'''

#float juga bisa dengan huruf eksponen E atau e untuk menunjukkan pangkat 10
'''
x = 25e2
y = 15E4
z = -50.6e100
print(type(x))
print(type(y))
print(type(z))
'''

#complex Bilangan kompleks ditulis dengan huruf "j" sebagai bagian imajiner:
'''
p = 3+5j
r = 5j
z = -5j
print(type(p))
print(type(r))
print(type(z))
'''

#konversi tipe
'''
dapat mengkoversi/mengubah dari satu tipe data ke tipe data lain
 dengan metode int(), float(), dan complex()
'''
'''
x = 10   # int
y = 3.5  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
'''

#Random Number
#digunakan untuk menghasilkan angka acak

import random

print(random.randrange(1, 10))  #menghasilkan angka acak antara 1 dan 9
