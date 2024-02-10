# Create a string containing your first and last name. Use one of the built-in string functions explained in the "Strings" 
#portion of the platform to check to see if that string contains your last name

fullName = 'Kathy Bailey Hines'
# look for my last name
index = fullName.find('Bailey Hines')
countOccurrence = fullName.count('Bailey Hines')
if countOccurrence > 0:
    #f is used to embed {}
    print(f"Last name is present {countOccurrence} time(s)")
else:
    print("Last name is not present.")


#Create a user name. Your user name must contain letters and numbers ONLY. Use one of the built-in string functions 
#explained in the previous slide to check to see if that string is valid.

import random

#"def" keyword is used to declare a function.
def getRandomUsername(length):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    # start with empty string for username
    username = ''

    # repeat length times/in this example it's 8 times
    for i in range(length):
        # pick random character to add to username
        randomCharacter = random.choice(characters)
        username += randomCharacter

    return username

# length is 8 to avoid endless loop
randomUsername = getRandomUsername(8)
print('Random Username: ', randomUsername)