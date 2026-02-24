#Python Polymorphism

#string
p = "Haalooo semuanyaaa..."

print(len(p))


#tuple
mytuple = ("cupcake", "brownies", "donat")

print(len(mytuple))


#dictionary
thisdict = {
  "jenis": "brownies",
  "rasa": "manis",
  "ukuran": "medium",
  "harga": 15000
}

print(len(thisdict))


#Class Polymorphism

class Mobil:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model

  def pergerakan(self):
    print("Kemudikan!")

class Perahu:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model

  def pergerakan(self):
    print("Berlayar!")

class Pesawat:
  def __init__(self, merek, model):
    self.merek = merek  
    self.model = model

  def pergerakan(self):
    print("Terbang!")

mobil1 = Mobil("Ford", "Mustang")       #membuat objek Mobil  
perahu1 = Perahu("Ibiza", "Touring 20") #membuat objek Perahu
pesawat1 = Pesawat("Boeing", "747")     #membuat objek Pesawat
for x in (mobil1, perahu1, pesawat1):
  x.pergerakan()


#Inheritance Class Polymorphism

class Kendaraan:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model

  def pergerakan(self):
    print("Jalan!")

class Mobil(Kendaraan):
  pass

class Perahu(Kendaraan):
  def pergerakan(self):
    print("Berlayar!")

class Pesawat(Kendaraan):
  def pergerakan(self):
    print("Terbang!")

mobil1 = Mobil("Ford", "Mustang") 
perahu1 = Perahu("Ibiza", "Touring 20") 
pesawat1 = Pesawat("Boeing", "747")

for x in (mobil1, perahu1, pesawat1):
  print(x.merek)
  print(x.model)
  x.pergerakan()
