# and operator
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = int(input('Ingrese el número de stock =>'))

print(stock >= 100 and stock <= 1000)


# or operator
print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)

role = input('Digital el rol =>')
print(role == 'admin' or role == 'seller')

# Ternary Condition
print('Hay stock' if stock > 5  else 'No hay stock')