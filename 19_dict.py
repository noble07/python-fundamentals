# Dictionaries are key value pairs, what in other lenguages are called 'associative array'
my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': 'asdfasdf',
    'name': 'Juan Camilo',
    'last_name': 'Muñoz Zuleta',
    'age': 25
}

print(my_dict)
print(len(my_dict)) # Returns dictionary length
print(my_dict['name']) # Returns the value associated with the key
print(my_dict['last_name'])
print(my_dict.get('age')) # Also returns the value but if not exist return None
print(my_dict.get('fasd')) # Returns None

print('avion' in my_dict) # Checks if the key exists in the dictionary
print('otroqueno' in my_dict)