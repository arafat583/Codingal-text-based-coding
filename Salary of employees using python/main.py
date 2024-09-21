def employee(name):
    print(name)

def salary(exp):
    if exp >= 5:
        return 3000000
    elif exp >= 3:
        return 1000000
    else:
        return 50000

employee("Steve")
s = salary(15)
print(f"The salary of employee is {s}") 
