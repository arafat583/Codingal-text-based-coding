with open('Codingal.txt', 'w') as file:
     file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

with open('Codingal.txt', 'r') as file:
     txtfile = file.readlines()
     print("Words in this file are....")
     for line in txtfile:

         word = line.split()
         print (word)
file.close()

new_file = open('writtencode.txt', 'x')
new_file.close()

import os
print("checking if my_file exists or not")
if os.path.exists("replcode.txt"):
    os.remove("replcode.txt")
else:
    print("This file doesn't exists")    


my_file = open('myfile.txt', 'w')
my_file.write("Hi! I am Penguin and I am 1 year old")
my_file.close()

os.remove('codingal.txt')

os.rmdir('writto')

outputFile = open('NotRepeated.txt', "w")

inputFile = open('Repeated.txt', "r")

varyble = set()
print("Eliminating duplicate lines....")

for line in inputFile:
    if line not in varyble:
       outputFile.write(line) 
       varyble.add(line)

inputFile.close()
outputFile.close()
