my_set = {1, 2, 3}
print(my_set)

my_set = {1.0, "Hello", True, (1, 2, 3)}
print(my_set)

my_set = {1, 2, 3, 4, 2, 1, 3, 5, 6, 6, 7}
print(f"{my_set}. \n")

num_set = set([1, 2, 3, 4, 5])
print(f"Original set: {num_set}")
num_set.pop()
print(f"After removing the first element from the set: {num_set}\n")