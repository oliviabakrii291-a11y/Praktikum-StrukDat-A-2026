class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        

class Karyawan(Person):
    def __init__(self, name, gender, age, gaji):
        super().__init__(name, gender, age)
        self._gaji = gaji #protected

    def get_gaji(self):
        return self._gaji
    
    def set_gaji(self, gaji):
        self._gaji = gaji
    


class Rekening:
    def __init__(self, norek, pin):
        self.noRek = norek
        self.__pin = pin

    def set_pin(self,pin):
     if pin > 5:
        self.__pin = pin
     else:
        print("pin must be more than 5 words")
    
    def get_pin(self):
        return self.__pin
    

    
p1 = Karyawan("Pia Mantap", "Female", 20, 5000000)
r1 = Rekening("1234", "asdfg")

print(r1.get_pin())
print(p1.name)
print(p1.get_gaji())

     