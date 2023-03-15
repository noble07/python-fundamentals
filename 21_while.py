""" 
while True:
    print('se ejecuto')

counter = 0

while counter < 10:
    counter += 1
    print(counter)


counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break # break keyword stop the loop
    print(counter)
"""

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue # Jumps to the next cicle stoping the execution of the current loop
    print(counter)