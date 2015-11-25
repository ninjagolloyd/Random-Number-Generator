#Written by Stephen (Jack) Henry
#Python methods used/exercised:
# 1. Importing modules (import)
# 2. ErrorHandling (While/Except) Statement
# 3. Saving a variable as a int (Interger) int() eg. str()
# 4. 'if' and 'and' statements

import random
import time

RNG = 1
#Scope = UserDefined int
n1 = 0
n2 = 0
n3 = 0
n4 = 0

print("(R)andom (N)umber (G)enerator 2.0")
print('')
print('Please select the scope of the numbers')
print('If you want to generate a 4 digit pin use 0 and 9 with a 4 random numbers')
print('')

#First Number: With Error Handling if the user puts in letters. 
while True:
    try:
        n1 = int(input('Pick your first number: '))
        break
    except ValueError:
        print("Oops! Please enter a valid number. Try again...")

#Second Number: With Error Handling if the user puts in letters. 
while True:
    try:
        n2 = int(input('Pick your second number: '))
        break
    except ValueError:
        print("Oops! Please enter a valid number. Try again...")

#Statement to show the numbers the user has chosen with lowest going first
if n1 < n2:
    print('Your lowest possible number is:', n1, 'and your highest possible number is:', n2)
else:
    print('Your lowest possible number is:', n2, 'and your highest possible number is:', n1)

# There must be a better way: This section rearranges the numbers from lowerst to highested for the RNG generator.
if int(n1) < int(n2):
    n3 = n1
if int(n1) < int(n2):
    n4 = n2
if int(n1) > int(n2):
    n3 = n2
if int(n1) > int(n2):
    n4 = n1

# I used the following lines to test the if statements (I found out there were not saving the varible when I added an else statement to it)
#print(n3)
#print(n4)
#time.sleep(3)

# Writing in smart detection of numbers: There must be a better way.
if n1 == 1 and n2 == 6 :
    print('You have chosen to role a six sided die')
if n2 == 1 and n1 == 6 :
    print('You have chosen to role a six sided die')
if n1 == 0 and n2 == 9 :
    print('You have chosen to generate a single digit number')
if n2 == 1 and n1 == 9 :
    print('You have chosen to generate a single digit number')

print('')
Scope = int(input('How many random numbers do you want? '))
Scope = Scope + 1 # This is so the RNG number listing starts at 1 and not 0
print('')

# This is some fluff
print('')
print('Generating', Scope, 'RNG Variables!')
time.sleep(.5)
print("Forcing the RNG Monkey to work for it's food...")
time.sleep(1)
print('')

#RNG Output Section
while RNG < Scope :
    print('RNG number:', RNG, 'is...', random.randint(int(n3), int(n4)))
    time.sleep(.9)
    RNG += 1 # This is the same thing as RNG = RNG + 1

#Ending Statements Below
print('')
print('Numbers generated in:', Scope*.9, 'seconds')
print('To generate more numbers please restart this application')
print('')
