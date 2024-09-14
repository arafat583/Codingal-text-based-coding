file_read = open('coding.txt', 'r' )
print("the file is in reading mode:\n")
print(file_read.read())
file_read.close()

file_write = open('coding.txt', 'w' )
print("the file is in writing mode:\n")
print(file_write.write("Hows your day going?"))
file_write.close()

file_append = open('coding.txt' , 'a' )
print("the file is in appending mode:\n")
print(file_append.write("Where do you live"))
file_append.close()