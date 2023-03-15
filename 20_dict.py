person = {
    'name': 'juan',
    'last_name': 'muñoz',
    'langs': ['javascript', 'python'],
    'age': 25
}

print(person)

# Changing a value of the dict.
person['name'] = 'camilo'
person['age'] -= 5
person['langs'].append('rust')
print(person)

# Remove an item 
# del keyword (this can be use with lists as well)
del person['last_name']

# pop() remove and item with the specified key and returns the value
person.pop('age')
print(person)


# Dict Methods
# items() returns a set-like (like a tuple) object for each key-value pair
print('items')
print(person.items())

# keys() returns a set-like (like a list) object with the keys
print('keys')
print(person.keys())

# values() returns a set-like (like a list) object with the values
print('values')
print(person.values())