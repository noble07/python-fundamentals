""" 
for element in range(1, 21): # range(start, stop) return produces a sequence of integers 
    print(element)
"""

# Looping through lists
my_list = [23, 45, 56, 356]

for element in my_list:
    print(element)

# Looping through touples
my_tuple = 'juan', 'camilo', 'patricia'
for i in my_tuple:
    print(i)

# Looping through dictionaries
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for k, v in product.items(): # items() returns a tuple for each key-value pair and gets unpack
    print(k, '=>', v)

# Similar to wat we get when querying a db
people = [
    {
        'name': 'juan',
        'age': 34
    },
    {
        'name': 'patricia',
        'age': 25
    },
    {
        'name': 'camilo',
        'age': 45
    }
]

for person in people:
    print(person['name'])