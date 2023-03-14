# Creates a sequence of values (can be of diferent types), is mutable
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make dishes', 'play videogames']
print(tasks)

types = [1, True, 'Hello']
print(types)

# Access to the value in the especific position
print(numbers[0])
print(tasks[0])

# mutates the first element on the list
tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

# With list we can slice a part of the list
print(numbers[:3])

# in operator can also be use in a list to ckeck for values
print(True in types)
print('Hello' in types)