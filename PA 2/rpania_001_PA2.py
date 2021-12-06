#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 2
# Due Date: 9/9/2020
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
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#constants
pi = 3.14159

#shelter advice function
def seek_shelter(seconds, inside):
    #if inside, there is no need for the function to output "yes"(already inside)
    if seconds <= 25 and inside == False:
        return "yes"
    else:
        return "no"
 
#sleep and energy function
def energy(age, amt_sleep, cals_burned):
    #young is 30 and under
    if age <= 30:
        #two hours more sleep for young -- calories
        if cals_burned > 2200:
            if 5 <= amt_sleep < 10:
                return "young and dazed"
            elif amt_sleep < 5:
                return "young and exhausted"
            else:
                return "young and rested"
        #at least eight hours of sleep to be rested
        else:
            if 4 <= amt_sleep < 8:
                return "young and dazed"
            elif amt_sleep < 4:
                return "young and exhausted"
            else:
                return "young and rested"
    #old is 60 and above
    elif age >= 60:
        #four hours more sleep for old -- calories
        if cals_burned > 1800:
            if 4 <= amt_sleep < 8:
                return "old and dazed"
            elif amt_sleep < 4:
                return "old and exhausted"
            else:
                return "old and rested"
        #at least four hours of sleep to be rested
        else:
            if 2 <= amt_sleep < 4:
                return "old and dazed"
            elif amt_sleep < 2:
                return "old and exhausted"
            else:
                return "old and rested"
    #middle aged is inbetween young and old (everything else)
    else:
        #three hours more sleep for middle aged -- calories
        if cals_burned > 2000:
            if 4.5 <= amt_sleep < 9:
                return "middle aged and dazed"
            elif amt_sleep < 4.5:
                return "middle aged and exhausted"
            else:
                return "middle aged and rested"
        #at least six hours of sleep
        else:
            if 3 <= amt_sleep < 6:
                return "middle aged and dazed"
            elif amt_sleep < 3:
                return "middle aged and exhausted"
            else:
                return "middle aged and rested"

# pizza function
def pizza_coverage(r_pizza, r_pep, num_pep):
    #find area of pizza, then find area of each pepperoni
    area_pizza = (r_pizza ** 2) * pi
    #multiply area of each pepperoni by num_pep to find its total area
    area_pep = (r_pep ** 2) * pi * num_pep
    #the fraction of the pizza coverage is multiplied by 100 for percentage
    percentage_pep = area_pep / area_pizza * 100
    if percentage_pep >= 75:
        return "happy customer"
    elif percentage_pep < 50:
        return "sad customer"
    else:
        return "neutral customer"