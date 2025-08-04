my_dict={'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict['name'])  
my_dict['age'] = 31
print(my_dict)
my_dict['grade']=10
print(my_dict)

print(my_dict)
print('address:',my_dict.get('city'))
my_dict.clear()
print(my_dict)