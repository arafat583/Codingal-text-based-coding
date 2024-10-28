class Employee():

    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")

def create_obj():
    print("Object making")
    obj = Employee()
    print("Function end...")
    return obj

print("Calling 'create_obj()' fujnction")
obj = create_obj()
print("Program End...")
        