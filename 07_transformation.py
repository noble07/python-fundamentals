# It dynamically changes variable type

name = "Juan"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Juan" + " Muñoz")
print(10 + 20)
# print("Juan" + 25) # Tries to concatenate and throws and error

age = 25
print("Mi edad es " + str(age)) # Doesn't throw error cause age is been transform to string
print(f"Mi edad es {age}") # f-string treats variables as string so there is no need to transform them

age = int(input("Escribe tu edad => ")) # int() Transform values to int (if input return an alphanumeric string it throws an error)
print(type(age))
print(f"Tu edad en 10 años será {age+10}") # If input is not transform this throws an error

print(type(not 0), not 0)