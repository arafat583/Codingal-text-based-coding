class student:

  grade = "6th"

  def __init__(self, name, father):
    self.name = name
    self.father = father


S1 = student("Arafat", "Mostafiz ")
S2 = student("Munabbir", "Md.Shariful Islam")

print("Student 1 is a student of".format(S1.grade))
print("Student 2 is a student of".format(S2.grade))

print("{} is son of {}".format(S1.name, S1.father))
print("{} is son of {}".format(S2.name, S2.father))