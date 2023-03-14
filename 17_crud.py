# CRUD Create, Read, Update, Delete

# Create
numbers = [1, 2, 3, 4, 5]

# Read
print(numbers[1])

# Update
numbers[-1] = 10
print(numbers)

# Adds an element to the end of the list
numbers.append(700)
print(numbers)

# Adds an elemente to the given position shifting the others elements to the right
numbers.insert(0, 'hola')
print(numbers)
numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']

# Join lists
new_list = numbers + tasks
print(new_list)

# Returns the index of value
index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

# Delete
new_list.remove('todo 1')
print(new_list)

# pop() Remove and returns the element at index (default is last)
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)

# reverse() reverse the list items
new_list.reverse()
print(new_list)

# sort() sort elements of a list (ascending default)
numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort() # Can't be sorted cause lists has values of different types