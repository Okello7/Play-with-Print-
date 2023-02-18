import os
import time

print()
print("")
print('')#Empty line
print('\n')#Blank  line
print("A line of text. \n")
print("A line of text.\n".rstrip())
print("A line of text1.")
print("Please wait while the program is loading...")
message = "Please wait while the program is loading..."
print(message.upper())


print("Hello " + os.getlogin() + '! How are you?')
use = os.getlogin()
print(f"Please {use} wait while the program is loading...")


print('Printing in a Nutshell', end='\n * ')
print('Calling Print', end='\n * ')
print('Separating Multiple Arguments', end='\n * ')
print('Preventing Line Breaks')

"""import sys
print(sys.stdin, sys.stdout, sys.stderr, sep=",", end = "\n *")"""


num_seconds = int(input("Enter seconds: "))

def sleeptime():
    for countdown in reversed(range(num_seconds + 1)):
        if countdown > 0:
            print(countdown, end='...')
            time.sleep(1)
        else:
            print('Go!')


sleeptime()

data = {'powers': [x**10 for x in range(10)]}
print(data)
