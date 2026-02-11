#booleans
#Tipe data Boolean mewakili salah satu dari dua nilai: Trueatau False.
'''
print(50 > 7)
print(11 == 11)
print(8 < 5)
'''

'''
a = 150
b = 55

if b > a:
  print("b lebih besar a")
else:
  print("b tidak lebih besar dari a")
  '''

#mengevaluasi nilai dan variabel
'''
print(bool("Halo"))
print(bool(15))

#evaluasi dua variabel

x = "mantap"
y = 30

print(bool(x))
print(bool(y))
'''

#Semua string adalah True, kecuali string kosong.
#Angka apa pun adalah True, kecuali 0.
#Semua list, tuple, set, dan dictionary adalah True, kecuali yang kosong.
'''
bool("aiueo")
print (bool("aiueo"))
bool(234)
print (bool(234))
bool(["ayam", "kucing", "sapi"])
print (bool(["ayam", "kucing", "sapi"]))
'''

#Contoh nilai yang dianggap False
'''
Sebenarnya, tidak banyak nilai yang dievaluasi menjadi False, 
kecuali nilai kosong, seperti (), [], {}, "", angka 0, dan nilai None.
Dan tentu saja nilai tersebut Falsedievaluasi menjadi False.
'''
'''
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''
'''
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
'''
#Contoh Kelas dengan Metode __len__()
'''
class KotakKosong:
    def __len__(self):
        return 0

kotak = KotakKosong()
print(bool(kotak)) 
'''
#fungsi dapat mengembalikan nilai boolean
'''
def kotakKosong() :
  return True
print(kotakKosong())
'''

'''
def kotakKosong() :
  return True

if kotakKosong():
  print("YES!")
else:
  print("NO!")
'''

'''
'''
'''
isinstance() fungsi `is_boolean_type`
yang dapat digunakan untuk menentukan 
apakah suatu objek memiliki tipe data tertentu
'''

#Periksa apakah suatu objek merupakan bilangan bulat atau bukan
x = 20.5
print(isinstance(x, int))
