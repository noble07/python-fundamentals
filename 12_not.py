# not operator negates the logical operation result

print(not True) # False
print(not False) # True

# and operator
print('NOT AND')
print('not True and True =>', not (True and True))
print('not True and False =>', not (True and False))
print('not False and True =>', not (False and True))
print('not False and False =>', not (False and False))

stock = int(input('Ingrese el número de stock =>'))

print(not (stock >= 100 and stock <= 1000))