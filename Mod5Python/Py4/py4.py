'''
Create a python guessing game using the input() function. The program should create a number variable that ranges from 1-10. 
Then use the input() function to have the user guess the number. If the number is too big print to the user “The number is too big guess again”,
If the number is too small print to the user “The number is too small guess again”. If the number is the correct number then print to the user 
that they guessed successfully. 
'''
#int - I want to use integers
import random
myNumber = random.randint(1, 10)

while True:
    yourNumber = int(input('Guess a number from 1-10:'))
    if yourNumber != myNumber:
        if yourNumber > myNumber:
            print('Too high! Guess again.')
        elif yourNumber < myNumber:
            print('Too low! Guess again.')
    else:
            print('You got it!')
            break # exit loop with correct guess
