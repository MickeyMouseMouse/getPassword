import sys
import random

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 
           'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
           'z', 'x', 'c', 'v', 'b', 'n', 'm']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
other = ['_', '+', '-', '*', '/', '.', ',', '>', '<', '=', 
         '|', '\\', ';', ':', '"', '[', ']', '{', '}',
         '&', '%', '$', '#', '!', '?', '^']

length = 15
if len(sys.argv) == 2:
    try:
        parameter = int(sys.argv[1])
    except ValueError:
        parameter = 0
        
    if (parameter >= 8): length = parameter    

for _ in range(length):
    mode = random.randint(0, 2)
    
    if (mode == 0):
        letter = letters[random.randint(0, 25)]
        if (random.randint(0, 1) == 1): letter = letter.upper()
        print(letter, end = "")
        continue
    
    if (mode == 1):
        print(numbers[random.randint(0, 9)], end = "")
        continue
    
    print(other[random.randint(0, 25)], end = "")

print()