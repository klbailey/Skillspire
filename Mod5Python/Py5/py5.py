# Prompt the user for a number between 1 and 3 (1=Rock, 2=Paper, or 3=Scissors)

yourNumber = int(input('Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '))

# Use the random number generator to generate a random number between 1 and 3

import random
myNumber = random.randint(1, 3)

# If the user chose a value that will beat the computer generated value then tell them that they have won. Other wise tell the user that they have lost
# rock beats scissors 1 > 3  / paper beats rock 2 > 1 / scissors beats paper 3 > 2

if (yourNumber == 1 and myNumber == 3) or (yourNumber == 2 and myNumber == 1) or (yourNumber == 3 and myNumber == 2):
    print('Winner winner chicken dinner!')
elif (yourNumber == myNumber):
    print("It's a tie.")
else:
    print('You lose. Better luck next time!')

# print(myNumber)