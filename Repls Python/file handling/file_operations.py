file = open('Codingal.txt', 'r')
print("file in read mode-")
print(file.read())
file.close()

file = open('Codingal.txt', 'w')
file.write("file in write mode-")
file.write("Hi! I am Penguin. I am 1 yr old")
file.close()

file = open('Codingal.txt', 'a')
file.write("\n the file is in append mode")
file.write("Hi! I am Penguin. I am 1 yr old")
file.close()