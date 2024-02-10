 # Prompt the user for how many units sold
units = int(input('How many number of units sold? '))

# Cost before discount
cost = units * 99

# 1-9 no discount / 10-19 20% / 20-49 30% / 50-99 40% / 100 or more 50%
# '{:.2f}' is {}placeholder for string : separator .2 number of decimals to display f float
if units < 10:
    print('Cost is ${:.2f}'.format(cost)) 
elif (units >= 10 and units < 20):
    withDiscount = (cost - (cost * .2))
    print('Cost is ${:.2f}'.format(withDiscount))
elif (units >= 20 and units < 50):
    withDiscount = (cost - (cost * .3))
    print('Cost is ${:.2f}'.format(withDiscount))
elif (units >= 50 and units < 100):
    withDiscount = (cost - (cost * .4))
    print('Cost is ${:.2f}'.format(withDiscount))
elif (units >= 100):
    withDiscount = (cost - (cost * .5))
    print('Cost is ${:.2f}'.format(withDiscount))
else:
    quit()
