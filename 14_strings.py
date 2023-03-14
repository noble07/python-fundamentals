text = 'Ella sabe programar en Python'
""" 
# in operator, checks if text exists with in a string
print('JavaScrilpt' in text)
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien!!')
else:
    print('También elegiste bien')
 """
# Returns the numbre of elements/characters including spaces
print(len(text))

# upper() returns a copy of the text in Upper case
print(text, text.upper())

# lower() returns a copy of the text in lower case
print(text, text.lower())

# count() returns the number of acurrences of the string in text
print(text.count('a'))

# swapcase() lower and upper case characters
print(text.swapcase())

# startswith() returns true if string starts with the given prefix
print(text.startswith('Ella'))

# endswith() returns true if string ends with the given prefix
print(text.endswith('Rust'))

# replace() returns a copy of the string with all ocurrences replaced by new string
print(text.replace('Python', 'Go'))

text2 = 'este es un titulo'
print(text2)

# capitalize() Capitalize string
print(text2.capitalize())

# title() returns a copy of the string with each word title case
print(text2.title())

# isdigit() returns true if the string is a digit in string format
print(text2.isdigit())