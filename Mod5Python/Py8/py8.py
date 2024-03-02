# Write a program that calculates the result using the following formula:
# result = 3? + 5? result=3x+5X Sample input x=3 y=4 result = 29

x = 3
y = 4

def formula(x, y):
    #calculate 3X + 5y
    result = 3 * x + 5 * y
    return result
# Call the formula function with the sample input values and store the result
result = formula(x, y)

print (result)

# This program should calculate the pay of an employee based on hours worked. The input includes the employee’s 
# total hours worked per week and their hourly pay rate. The employee will be paid a base wage for the first 40 hours 
# worked and time-and-a-half (150% of base pay) for any hours past 40 as overtime pay. Output the regular pay, 
# overtime pay, and total pay for the week on the screen.If the employee worked 40 hours or less, don’t show any output 
# regarding overtime pay.

def calculate_pay(hoursWorked, payRate):
    # find minimum value between 40 and hoursWorked result is smaller of the two
    regular_hours = min(40, hoursWorked)  # hours (up to 40 hours)
    # hoursWorked-40 is hours beyond regular 40 make sure non negative (thus 0 in first param)
    overtime_hours = max(0, hoursWorked - 40)  # overtime hours (hours beyond 40)

    regular_pay = regular_hours * payRate
    overtime_pay = overtime_hours * 1.5 * payRate  # Overtime pay is 1.5 times the hourly rate
    total_pay = regular_pay + overtime_pay

    # Display the results
    print(f"Regular pay: {regular_pay}")
    
    if overtime_hours > 0:
        print(f"Overtime pay: {overtime_pay}")
        
    print(f"Total pay: {total_pay}")

# Sample input 1
hoursWorked_worked_1 = 30
hourly_pay_rate_1 = 10
calculate_pay(hoursWorked_worked_1, hourly_pay_rate_1)

# Sample input 2
hoursWorked_worked_2 = 50
hourly_pay_rate_2 = 10
calculate_pay(hoursWorked_worked_2, hourly_pay_rate_2)
