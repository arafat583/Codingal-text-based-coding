 # file = open('codingal.txt', 'r')
with open('codingal.txt', 'r') as file:
  data = file.read()
  print(data)
file.close()  