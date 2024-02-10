# Print the sum of all the numbers from 1-15
# Indexing starts at 0 so range(start, stop) should be (1, 16) 
# excludes 0 includes/stops at number 15 which is index[16]
numberSum = sum(range(1, 16))
print('The sum of all the numbers from 1-15 is:', numberSum)

# Use a for loop to count from 1-100. For every number that is odd print “FIZZ” 
# for every number that is even print “BUZZ”
for i in range(1, 101):
    if i % 2 != 0:
        # print(f'{i} FIZZ')
        print('FIZZ')
    else:
        # print(f'{i} BUZZ')
        print('BUZZ')

# Create a list variable with 5 numbers and find the minimum, maximum and average of all those numbers. Then print them out.
varList = [5, 35, 3, 45, 2]
minNum = min(varList)
print(minNum)
maxNum = max(varList)
print(maxNum)
# Average is sum divided by count (90 / 5) in list - len(varList) gives the count 
avgNum = sum(varList) / len(varList)
print(avgNum)