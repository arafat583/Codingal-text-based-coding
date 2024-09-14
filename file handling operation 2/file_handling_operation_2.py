new_file = open('Newfile.txt', 'x')
new_file.close()

import os
print("checking if my_file wxists or not")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("This file doesn't exists")    


my_file = open('my_file.txt', 'w')
my_file.write("Hi! I am Penguin and I am 1 year old")
my_file.close()

os.remove('codingal.txt')

os.rmdir('folderr')