text = 'Ella sabe Python'

# Text has an index that can be access as a array notation
# This text[0] returns the first character of the string
print(text[0])
print(text[1])
#print(text[99999]) # Throws an error cause that index is out of range

print(text[-1]) # Returns last character of the string
# can be achived also using len()
print(text[len(text) - 1])

# Slicing - using ':' we can create substring based on the text
print(text[0:5])
print(text[10:16])
print(text[:10]) # The first part of the slices is a 0 when we don´t specify it

print(text[5:]) # Starts on index 5 and goes to the end

print(text[10:16:2]) # The third number indicates the number of jumps
print(text[::2]) # Returns every 2 jumps
print(text[16:9:-1]) # Slices backwards
print(text[::-1]) # Returns the string backwards