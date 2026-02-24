#inner classes
class Luar:
  def __init__(self):
    self.nama = "Kelas Luar"

  class Dalam:
    def __init__(self):
      self.nama = "Kelas Dalam"

    def display(self):
      print("This is the inner class")

outer = Luar()
print(outer.nama)
inner = outer.Dalam()
print(inner.nama)


#Accessing Inner Class from the Outside
class Luar:
  def __init__(self):
    self.nama = "Luar"

  class Dalam:
    def __init__(self):
      self.nama = "Dalam"

    def display(self):
      print("Haloo, ini adalah kelas dalam")

outer = Luar()
inner = outer.Dalam()
inner.display()


#Accessing Outer Class from Inner Class

class Luar:
  def __init__(self):
    self.nama = "Piaa"

  class Dalam:
    def __init__(self, luar):
      self.outer = luar

    def display(self):
      print(f"Nama dari kelas luar: {self.outer.nama}")

outer = Luar()
inner = outer.Dalam(outer)
inner.display()


#practical example
class Mobil:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model
    self.mesin = self.Mesin()

  class Mesin:
    def __init__(self):
      self.status = "Mati"

    def Mulai(self):
      self.status = "Berjalan"
      print("Mesin dinyalakan")

    def Berhenti(self):
      self.status = "Mati"
      print("Mesin dimatikan")

  def Berkendara(self):
    if self.mesin.status == "Berjalan":
      print(f"Berjalan dengan kendaraan {self.merek} {self.model}")
    else:
      print("Nyalakan mesin terlebih dahlu!")
car = Mobil("Toyota", "Corolla")
car.Berkendara()
car.mesin.Mulai()
car.Berkendara()


#Multiple Inner Classes
class Komputer:
  def __init__(self):
    self.prosesor = self.CPU()
    self.memori = self.RAM()

  class CPU:
    def proses(self):
      print("Memproses data...")

  class RAM:
    def simpan(self):
      print("Menyimpan data...")
computer = Komputer()
computer.prosesor.proses()
computer.memori.simpan()