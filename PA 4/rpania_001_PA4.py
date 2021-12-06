#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 4
# Due Date: 9/27/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, assignments are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Function computes the sum of all the divisors of n
def sum_divisors(n):
    # The sum of divisors starts at a value of 0
    sum_div_fin = 0
    # If n is less than 0, it runs through a loop with negative ranges
    # This will return a negative integer
    if n < 0:
        for z in range(n + 1, -1):
            if n % z == 0:
                sum_div_fin = sum_div_fin + z
        return sum_div_fin
    # If n is greater than 0, it runs through a loop with positive ranges
    # This will return a non-zero positive integer
    elif n > 0:
        for z in range(1, n + 1):
            if n % z == 0:
                sum_div_fin = sum_div_fin + z
        return sum_div_fin
    # If n is 0, it returns a integer value of 0
    else:
        return 0

#-------------------------------------------------------------------------------
# Function computes the product of the negative numbers in a list
def negative_product(nums):
    # Result must be set as 1 so the first num will not automaticall output to 0
    fin_neg_val = 1
    # The loop checks if every number in the list is negative
    for num in nums:
        # If the number is less than 0, the number is multiplied with the result
        if num < 0:
            fin_neg_val = fin_neg_val * num
    return fin_neg_val

#-------------------------------------------------------------------------------
# Function checks whether house can be heated to desired temperature
def heater(fuel, temp):
    # The while loop checks if temp is desired, and if not, it burns 1 fuel
    while temp < 80 and fuel > 0:
        fuel = fuel - 1
        temp = temp + 5
    # If temp is less than 80, the if-statement returns a string
    if temp < 80:
        return "failure, highest temp is " + str(temp)
    # If temp is greater than 80, the else-statement returns one of two strings
    else:
        if fuel > 0:
            return "success, " + str(fuel) + " leftover fuel!"
        else:
            return "success, no leftover fuel!"

#-------------------------------------------------------------------------------
# Function determines percentage of time spent doing a specific activity
def analyze(activity, time_period):
    time_w = 0
    time_f = 0
    time_b = 0
    time_s = 0
    #README -- Am I allowed to index lists?
    for letter in time_period:
        # The if-elif-else statements compare the input string with letters
        if letter == "w":
            time_w = time_w + 20
        elif letter == "f":
            time_f = time_f + 15
        elif letter == "b":
            time_b = time_b + 10
        else:
            time_s = time_s + 60
    # The if-elif-else statements compare the desired activity with letters
    if activity == "w":
        activity_time = time_w
    elif activity == "f":
        activity_time = time_f
    elif activity == "b":
        activity_time = time_b
    else:
        activity_time = time_s
    # The following lines calculate the percentage of time spent on activity
    total_time = time_w + time_f + time_b + time_s
    p_time_working = float(activity_time) / float(total_time) * 100
    return round(p_time_working, 2)

#-------------------------------------------------------------------------------
# Function counts number of steps taken to reach the beginning/end of the line
def travel(position, velocity, acceleration):
    # The number of steps start at 0
    num_step = 0
    # The while loop runs when the position is between 0 and 1000 (exclusive)
    while position > 0 and position < 1000:
        # The following lines calculate the change in position with respect to \
        #velocity and acceleration
        position = position + velocity
        velocity = acceleration + velocity
        num_step = num_step + 1
    # Once while loop ends, the number of steps is returned as an integer
    return num_step
    