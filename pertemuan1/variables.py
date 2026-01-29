#membuat variabel
a = 7
b = "Olivia"
print(a)
print(b)

#Casting
'''
menentukan atau mengganti tipe data variabel
'''
a = str(7)    #a akan jadi '7'
b = int(9)    #b akan jadi 9
c = float(5)  #c akan jadi 5.0

#melihat tipe data
a = 7
b = "Olivia"
print(type(a))
print(type(b))

#Single or Double Quotes / tanda kutip tunggal atau ganda
a = "Olivia"
#sama dengan
a = 'Olivia'

#Case-Sensitive
#peka terhdap huruf besar dan kecil
b = 9
B = "Pia" 
print(b)
print(B)
#b dan B adalah variabel yang berbeda


#Nama Variabel
nilaisatu = "World"
nilai_satu = "World"
_nilai_satu = "World"
nilaiSatu = "World"
NILAISATU = "World"
nilaisatu1 = "World"

#yang tidak boleh digunakan sebagai nama variabel
"""
2myvar 1satuvariabel = "World" /angka duluan
satu-variabel = "World" /pakai tanda -
satu variabel= "World" /ada spasi
"""

#nama variabel multi kata
#Camel Case
#Setiap kata, kecuali kata pertama, diawali dengan huruf kapital
nilaiSatu = "World"

#Pascal Case
#Setiap kata diawali dengan huruf kapital
NilaiSatu = "World"

#Snake Case
#Setiap kata dipisahkan oleh karakter garis bawah
nilai_satu = "World"

#Assign Multiple Values
#Banyak Nilai untuk Banyak Variabel
a, b, c = "Ayam", "Bebek", "Kambing"
print(a)
print(b)
print(c)

#Satu Nilai untuk Beberapa Variabel
x = y = z = "Pisang Goreng"
print(x)
print(y)
print(z)


#Output Variables
#print digunakan untuk mencetak nilai variabel
x = "Python mantap"
print(x)

#di dalam print menampilkan beberapa variabel, dipisahkan oleh koma
x = "Ayam"
y = "goreng"
z = "enak"
print(x, y, z)

#dapat menggunakan + operator untuk menampilkan beberapa variabel
x = "Ayam"
y = "goreng"
z = "enak"
print(x +y + z)

#untuk angka, + karakter berfungsi sebagai operator matematika
b= 7
c = 6
print(b + c)

'''
untuk menampilkan beberapa variabel dalam print 
adalah dengan memisahkannya dengan koma
'''
x = 10
y = "Yoyo"
print(x, y)


#Global Variables
#variabel yang dibuat di luar fungsi, dapat diakses didalam maupun diluar fungsi
x = "mantap"

def myfunc():
  print("Python is " + x)

myfunc()

'''
jika membuat variabel dengan nama yang sama didalam fungsi,
variabel didalam fungsi akan menjadi variabel lokal
'''
#variable global dengan nama yang sama akan tetap seperti semula
#global dan dengan nilai aslinya
x = "mantap"

def myfunc():
  x = "menyenangkan"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#The global Keyword
"""
ketika membuat variabel dalam fungsi, variabel tersebut menjadi lokal
dan hanya dapat digunakan dalam fungsi tersebut.
"""
#untuk membuat variabel global didalam fungsi, gunakan kata kunci global
def myfunc():
  global x
  x = "mantap"

myfunc()

print("Python is " + x)
