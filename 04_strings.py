name = "Juan Camilo"
last_name = "Muñoz Zuleta"

print(name)
print(last_name)

# Concat strings
full_name = name + " " + last_name
print(full_name)

# Use double quotes if text contains apostrophes
quote = "I'm Juan"
print(quote)

# Use single quotes if text contains double quotes
quote2 = 'She said "Hello"'
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2', template)

# f-string
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', template)