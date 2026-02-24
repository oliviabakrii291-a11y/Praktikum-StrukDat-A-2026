#membuat parent class
class Nama:
    def __init__(self, depan, belakang):
        self.nama_depan = depan
        self.nama_belakang = belakang
    def printnama(self):
        print(self.nama_depan, self.nama_belakang)

x = Nama("Olivia", "Bakri")
x.printnama()
x = Nama("Ghea", "Ananda")
x.printnama()



#membuat child class
class Nama:
    def __init__(self, depan, belakang):
        self.nama_depan = depan
        self.nama_belakang = belakang
    def printnama(self):
        print(self.nama_depan, self.nama_belakang)


class Mahasiswa(Nama):
  def __init__(self, depan, belakang):
    super().__init__(depan, belakang)

x = Mahasiswa("Olivia", "Bakri")
x.printnama()

#pakai pass
class Mahasiswa(Nama):
    pass


#Add the __init__() Function
class Nama:
    def __init__(self, depan, belakang):
        self.nama_depan = depan
        self.nama_belakang = belakang

    def printnama(self):
        print(self.nama_depan, self.nama_belakang)


class Mahasiswa(Nama):
  def __init__(self, depan, belakang):
    Nama.__init__(self,depan, belakang)

x = Mahasiswa("Olivia", "Bakri")
x.printnama()



#Use the super() Function
class Nama:
    def __init__(self, depan, belakang):
        self.nama_depan = depan
        self.nama_belakang = belakang

    def printnama(self):
        print(self.nama_depan, self.nama_belakang)


class Mahasiswa(Nama):
  def __init__(self, depan, belakang):
    super().__init__(depan, belakang)

x = Mahasiswa("Olivia", "Bakri")
x.printnama()


#add properties
class Nama:
    def __init__(self, depan, belakang):
        self.nama_depan = depan
        self.nama_belakang = belakang

    def printnama(self):
        print(self.nama_depan, self.nama_belakang)


class Mahasiswa(Nama):
  def __init__(self, depan, belakang, tahun):
    super().__init__(depan, belakang)
    self.tahun_lulus = tahun

x = Mahasiswa("Olivia", "Bakri", 2029)
print(x.tahun_lulus)


#add methods
class Nama:
    def __init__(self, depan, belakang):
        self.nama_depan = depan
        self.nama_belakang = belakang

    def printnama(self):
        print(self.nama_depan, self.nama_belakang)


class Mahasiswa(Nama):
  def __init__(self, depan, belakang, tahun):
    super().__init__(depan, belakang)
    self.tahun_lulus = tahun

  def selamat(self):
    print("Selamat yaa", self.nama_depan, self.nama_belakang, "atas kelulusannya di tahun ", self.tahun_lulus)

x = Mahasiswa("Olivia", "Bakri", 2029)
x.selamat()
