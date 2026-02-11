#tanda kutip tunggal atau tanda kutip ganda
print("Alloo guyss")
print('Alloo guyss')


#kutipan dalam kutipan
print("Aman Aja")
print("Aku dipanggil 'Olip'")
print('Aku dipanggil "Olip"')

#Assign String to a Variable / menetapkkan string ke variabel
c = "halo teman"
print(c)

#Multiline Strings / string banyak baris
#bisa juga menggunakan tiga tanda kutip ganda
a = """Halo semuanya,
namaku Olivia 
prodiku Teknik Informatika."""
print(a)

#atau menggunakan tiga tanda kutip tunggal
a = '''Halo semuanya,
namaku Olivia 
prodiku Teknik Informatika.'''
print(a)

#string adalah array
'''Python tidak memiliki tipe data karakter, satu karakter hanyalah sebuah string dengan panjang 1.
Tanda kurung siku dapat digunakan untuk mengakses elemen-elemen dalam string.
'''

#ambil karakter pada posisi 1 (ingat bahwa karakter pertama berada pada posisi 0)
b = "Hello, World!"
print(b[1])

#melakukan perulangan melalui sebuah string
#menggunakan for loop
for x in "ayam":
    print(x)    

#String Length / panjang string
a = "Halo, Pia!"
print(len(a))   

#Check String / memeriksa string
txt = "mantap jiwa"
print("mantap" in txt)
#if jika pernyataan
if "jiwa" in txt:
    print("iya, 'jiwa' ada di dalam txt")   

#Check if NOT / memeriksa jika tidak ada
txt = "mantap jiwa"
print("mantap" not in txt)
#if jika pernyataan
if "hebat" not in txt:
    print("tidak, 'hebat' tidak ada di dalam txt")  

#Slicing / mengiris string
'''tentukan indeks awal dan indeks akhir, 
dipisahkan dengan titik dua (:), 
untuk mendapatkan sebagian string
'''
b = "Helloo, Guyss!"
print(b[2:5])

#slicing dari awal
b = "Helloo, Guyss!"
print(b[:5])

#slicing sampai akhir
b = "Helloo, Guyss!"
print(b[2:])

#Negative Indexing / pengindeksan negatif
b = "Helloo, Guyss!"
print(b[-5:-2])

#Upper Case
#mengubah huruf kecil menjadi huruf besar
a = "halo pia"
print(a.upper())    

#Lower Case
#mengubah huruf besar menjadi huruf kecil   
a = "HALO PIA"
print(a.lower())    

#Remove Whitespace / menghapus spasi
a = "  Halo Pia  "
print(a.strip())    #menghapus spasi di awal dan akhir string   

#Replace String / mengganti string
a = "Halo Pia"      
print(a.replace("H", "J"))
#mengganti H dengan J   

#Split String / memisahkan string
a = "Halo,Pia,Aku,Olivia"
print(a.split(","))   #memisahkan string di setiap koma



#untuk menambahkan space di antara dua string, gunakan " "
a = "Halo"
b = "Pia"
c = a + " " + b
print(c)  

#Format String
#gunakan format() untuk menyisipkan angka ke dalam string
age = 20
txt = f"Halo namaku Olivia, aku berumur {age}"
print(txt)

#gunakan placeholder {} dan modifier format()
#placeholder {} dapat berisi variabel, operasi, fungsi, dan mengubah untuk memformat nilai 
price = 100
txt = f"Harga tas {price} rupiah"
print(txt)

"""Sebuah pengubah disertakan dengan menambahkan titik dua :
diikuti oleh jenis format yang sah, seperti .2f
yang berarti angka titik tetap dengan 2 desimal
"""
price = 100
txt = f"Harga tas {price:.2f} rupiah"
print(txt)

#lakukan operasi matematika lalu kembalikan hasilnya
txt = f"Harga tas {20 * 5} rupiah"
print(txt)

#Escape Characters / karakter pelolosan
'''
escape characters digunakan untuk memasukkan karakter khusus
'''
txt = "Kita pasti bisa \"mendaki\" ke gunung Rinjani"
print(txt)
