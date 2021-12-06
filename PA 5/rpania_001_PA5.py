#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 5
# Due Date: 10/5/2020
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
#Function replaces "I’m" and "you’re" with "I am" and "you are"
def replace_contraction(text):
    ntext = ""
    x = 0
    #Loops until all elements of text are covered
    while x <= len(text) - 1:
        #If there are enough string characters left for "you're", "you're" is \
        #checked for, and translated if in the string (translated to new srting)
        #If "you're" is not in the string, "I'm" is checked for, and translated\
        #, if in the string (translated to new string)
        #If neither of these are true, the character text[x] is added to the \
        #string
        if x + 5 <= len(text) - 1:
            if (text[x] + text[x + 1] + text[x + 2] + text[x + 3] + \
            text[x + 4] + text[x + 5]) == "you're":
                ntext += "you are"
                x += 6
            elif x + 3 <= len(text) - 1:
                if (text[x] + text[x + 1] + text[x + 2]) == "I'm":
                    ntext += "I am"
                    x += 3
                else:
                    ntext += text[x]
                    x += 1
            else:
                ntext += text[x]
                x += 1
        #If there are enough string characters left for "I'm,", "I'm" is \
        #checked for, and translated, if in the string (translated to \
        #(new string)
        #If this is not true, the character text[x] is added to the string
        elif x + 3 <= len(text) - 1:
            if (text[x] + text[x + 1] + text[x + 2]) == "I'm":
                ntext += "I am"
                x += 3
            else:
                ntext += text[x]
                x += 1
        #the character text[x] is added to the string
        else:
            ntext += text[x]
            x += 1
    #Outputs the new string
    return ntext
#-------------------------------------------------------------------------------   
#Function swaps the position of adjacent items of numbers - length is even
def swap_adjacent(numbers):
    index = 0
    #Loops through numbers and replaces the xth odd index, then the xth even index \
    #until it reaches the last even index element
    while index <= len(numbers) - 2:
        a = numbers[index]
        b = numbers[index + 1]
        #a is replaced with b and b is replaced with a
        a,b = b,a
        #The elements are replaced in numbers
        numbers[index] = a
        numbers[index + 1] = b
        index += 2
#-------------------------------------------------------------------------------
#Function returns a new list with values less than one standard deviation from \
#the mean (in the same order as given)
def within_1_sd(numbers):
    variances = []
    sum_num = 0
    for num in numbers:
        sum_num += num
    #The mean determined by taking the average of all elements in numbers
    mean = sum_num/len(numbers)
    #Loops through all elements in numbers and calculates the difference \
    #between the element and the mean, and squares the value after
    #This is then added to a separate list
    for x in numbers:
        variances.append((x - mean) ** 2)
    sum_var = 0
    for var in variances:
        sum_var += var
    #The average of all values in variances is then square rooted to find \
    #standard deviation
    variance = sum(variances)/len(variances)
    std_dev = variance ** (1/2)
    std_dev_list = []
    for x in numbers:
        if (mean - std_dev) < (x) < (mean + std_dev):
            std_dev_list.append(x)
    return std_dev_list
#-------------------------------------------------------------------------------
#Function checks whether the following x numbers sum up to an initial value
#The value x starts as 2 but increases by 1 once the first 2 are summed \
#(the next 3 after the first 2 would be summed)
def equal_sum(numbers):
    count = 2
    index = 1
    first_val = numbers[0]
    #The loop runs as long as there are enough numbers to cover the whole list
    while index <= len(numbers)-count:
        compare_val = 0
        difference = 0
        #Loops through count number of times and creates a value to compare \
        #to the first value
        for num in range(count):
            compare_val += numbers[index + difference]
            difference += 1
        #If the values are equal, then the outer loop is continued
        if compare_val == first_val:
            count += 1
        #If the values are inequal, then False is returned
        else:
            return False
        index += (count - 1)
    #If the outer loop finishes running, True is returned
    return True
#-------------------------------------------------------------------------------
#Function checks whether a list has consecutive numbers or not
def is_sequence(numbers):
    min_val = numbers[0]
    x = 0
    #Loops through every num in numbers to determine the minimum value
    for num in range(len(numbers)):
        if numbers[num] <= min_val:
            min_val = numbers[num]
    #Outer loop incrementally increases index
    #Inner loop adds index to min_val and compares to every num in numbers  
    for index in range(len(numbers) - 1):
        temporary = False
        for num in numbers:
            #If the boolean is True, index is increased in the outer loop \
            #and the inner loop repeats
            if num == min_val + index:
                temporary = True
                break
        if temporary == False:
            return temporary
    return temporary