# Tuples are a sequence of values
# It's a sequence of INMUTABLE data
# It can be set just comma separated or with parentheses
numbers = 1, 2, 3, 4, 5
strigns = ('juan', 'camilo', 'muñoz', 'juan')
print(numbers) # on output are always enclosed in parentheses
print(type(numbers))
print(strigns)

# Accessing a tuple element, it can be done as a list
print('2 =>',numbers[2])
print('last =>',numbers[-1])

# Tuples may be nested
new_tuple = numbers, strigns
print(new_tuple)

# Tuple unpacking
n1, n2, n3, n4, n5 = numbers
print(n2)
n2 = 5
print(n2)

# Tuple methods
print(strigns)
print(strigns.index('camilo'))
print(strigns.count('juan')) # Returns the number of ocurrences of value

# It can be transform to a list to mutate data
my_list = list(strigns)
print(my_list)
print(type(my_list))

my_list[1] = 'cami'
print(my_list)

# And we can transform a list into a tuple to!
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))