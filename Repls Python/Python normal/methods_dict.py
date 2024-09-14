my_dict = {}

my_dict = {1: 'apple', 2: 'mango'}

my_dict = {'name': 'Robin', 'age': 20}

my_dict = {'name': 'Jack', 1: [2, 3, 4]}

my_dict = {'name': 'Jack', 'age': 26, 'address': 'peston ville'}

print(my_dict)
print(my_dict['name'])

my_dict['age'] =  27 
print(my_dict)

my_dict['address'] = 'Downtown'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print('Adress:', my_dict.get('address'))

my_dict.clear()
print(my_dict)