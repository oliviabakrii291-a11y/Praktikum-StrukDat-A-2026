#privat
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.__umur = umur # porperti privat

p1 = Orang("Olivia Bakri", 20)
print(p1.nama)
print(p1.__umur) # ini akan menyebabkan error karena __umur adalah properti privat


#mendapatkan privat dengan getter
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.__umur = umur

  def get_umur(self):
    return self.__umur

p1 = Orang("Olivia Bakri", 20)
print(p1.get_umur())



#set
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.__umur = umur

  def get_umur(self):
    return self.__umur

  def set_umur(self, umur):
    if umur > 0:
      self.__umur = umur
    else:
      print("Umur harus positif")

p1 = Orang("Olivia Bakri", 20)
print(p1.get_umur())

p1.set_umur(26)
print(p1.get_umur())  


#protected
class Orang:
  def __init__(self, nama, gaji):
    self.nama = nama
    self._gaji = gaji # properti protected

p1 = Orang("Olivia Bakri", 50000)
print(p1.nama)
print(p1._gaji) # ini bisa diakses, tapi sebaiknya tidak diakses langsung karena ini adalah properti protected

#name mangling
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.__umur = umur

p1 = Orang("Olivia Bakri", 20)

# Name mangling memungkinkan kita untuk mengakses properti privat dengan cara yang tidak direkomendasikan
print(p1._Orang__umur)  # tidak disarankan,
