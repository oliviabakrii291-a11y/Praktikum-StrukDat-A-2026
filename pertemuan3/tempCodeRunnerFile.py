class Animal:
  def __init__(self, name):
    self.name = name

    def Speak(self):
      print(self.name)


class Dog(Animal):
  print(self.name)
  
d1 = Dog("Rex")
d1.Speak()