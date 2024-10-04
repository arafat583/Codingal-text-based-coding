L = [4, 5, 1, 2, 9, 7, 10, 8]
print(f"Original List: {L}")

count = 0

# Finding the sum
for i in L:
    count += i  

# Divide the total elements by
# number of elements
avg= count/len() 

print(f"sum = {count}")
print(f"average = {avg}")

L.sort()

print(f"First element is: {L[0]}")
print(f"Last element is: {L[-1]}")





