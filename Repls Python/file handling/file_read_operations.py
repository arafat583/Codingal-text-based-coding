file = open('Codingal.txt','r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print('\n read in parts \n')
print(file.read(8))
file.close()

file = open('Codingal.txt','a')
file.write("Hi im a penguin and i am 1 year old")
file.close()