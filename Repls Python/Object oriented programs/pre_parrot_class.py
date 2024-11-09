class parrot: 
  def __init__(self, age, name):
      self.name = name
      self.age = age

  def sing(self, song):
      return "{} sings {}".format(self.name, song)

  def dance(self):
      return "{} is now dancing".format(self.name)

blu = parrot(10, "Blue")

print(blu.sing("'Happy'"))
print(blu.dance())