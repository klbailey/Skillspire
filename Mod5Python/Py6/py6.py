import random

def rollDice():
    # Prompt the user for a value between 1 and 6
    yourDice = int(input('Enter a number between 1 and 6: '))
    # Validate input
    if yourDice < 1 or yourDice > 6:
        print("Invalid input. Enter a number between 1 and 6: ")
        return rollDice()

    # Variables needed to print number of tries and successfully rolled 
    rolls = 0
    result = 0

    # Emulate dice rolling session. while loop result starts at 0 and continues looping until random number matches number entered from user prompt
    while result != yourDice: 
        result = random.randint(1, 6) #gets random number
        rolls += 1 #attempts
        print(f"You rolled {result}")   

    # If the user rolls the number that they were prompted for 
    print(f"Congrats! You have successfully rolled a {yourDice} in {rolls} attempts.")

# Call function
rollDice()