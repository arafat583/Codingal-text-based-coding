# tuple = first bracket - ()
# dictionary = third bracket - {}
# set = third bracket - {}
# list - second bracket - []
# array - third bracket - {}

# Code:

import array as arr

array_num = arr.array('i',[1, 2, 3, 4, 3, 5, 6, 3])
print(f"Original array: {str(array_num)}")

print(f"Number of occurences of NUmber 3 in the given array {str(array_num.count(3))}")

array_num.reverse()
print(f"Reverse the order of the items: {str(array_num)}")