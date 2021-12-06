#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 7
# Due Date: 9/20/2020
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, assignments are individual effort!r
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
def create_3DFill(info):
    """This function creates a list of list of lists"""
    return_list = []
    #Checks if | is in the input
    count = 0
    if "|" in info:
        count += 1
    if count != 1:
        return return_list
    #Makes a list with the input string, splitting at "|"
    info_string = info.split("|")
    #Creates a list that contains all numbers and "x"s
    numbers = []
    for x in range(len(info_string[1])):
        if info_string[1][x] != " ":
            numbers.append(info_string[1][x])
    info_string[1] = numbers
    #Reassigns info_list
    info_list = [info_string[0], "|"]
    for number in numbers:
        info_list.append(number)
    #Creates a list for the dimensions by looping through numbers
    number_str = ""
    #Replaces uppercase "X"s with lowercase "x"s
    for number in range(len(numbers)):
        if numbers[number] == "X":
            numbers[number] = numbers[number].lower()
    for number in numbers:
        number_str += number
    dimensions = number_str.split("x")
    #Removes whitespace from outside of first element
    rem_str = ""
    rem_whit_out = info_list[0].split() 
    for x in range(len(rem_whit_out)):
        rem_str += rem_whit_out[x]
    info_list[0] = rem_str
    #Removes parenthesis from first element
    info_list_string = ""
    character = 1
    #Loops through every character except the first and last of info_list[0]
    while character < len(info_list[0]) - 1:
        info_list_string += info_list[0][character]
        character += 1
    #Checks if there are less elements than the valid number of dimensions
    if len(dimensions) != 3:
        return return_list
    #Checks for missing parentheses
    count = 0
    if "(" in info_list[0]:
        count += 1
    if ")" in info_list[0]:
        count += 1
    if count != 2:
        return return_list
    #Removes parenthesis and spacing by replacing the element with the string
    info_list[0] = info_list_string
    #Checks for missing "x"s
    count = 0
    for element in info_list:
        if element.isdigit() == False:
            if element.lower() == "x":
                count += 1
    if count != 2:
        return return_list
    #Checks if dimensions are numeric values / whether they are missing 
    count = 0
    for element in dimensions:
        if element.isdigit() == True:
            count += 1
    if count < 3:
        return return_list
    #Checks if dimensions are negative
    count = 0
    for element in info_list:
        if element.isdigit() == True:
            if int(element) < 0:
                count += 1
    #Turns row, col, and depth into integers
    dimensions[2] = int(dimensions[2])
    dimensions[0] = int(dimensions[0])
    dimensions[1] = int(dimensions[1])
    if count > 0:
        return return_list
    else:
        #If row and depth are 0, a value is returned
        if dimensions[2] == 0 and dimensions[1] == 0:
            return info_list[0]
        else:
            #Loops through the range of depth
            for depth in range(dimensions[2]):
                depth_section = []
                return_list.append(depth_section)
                #Loops through the range of row
                for row in range(dimensions[0]):
                    row_section = []
                    depth_section.append(row_section)
                    #Loops through the range of col
                    for column in range(dimensions[1]):
                        row_section.append(info_list[0])
    return return_list
#-------------------------------------------------------------------------------
def categorize_info(lst):
    """Thus function creates and organizes list of lists"""
    #Creates a lists of people with the same age
    ages = []
    row = 0
    #Loops through the given list to find all available ages
    while row < len(lst):
        if lst[row][1] not in ages:
            ages.append(lst[row][1])
        row += 1
    age_list = []
    #Loops through all of the available ages and adds them to a list with \
    #people that are that age
    for age in ages:
        age_section = []
        age_list.append(age_section)
        age_section.append(age)
        row = 0
        while row < len(lst):
            if lst[row][1] == age:
                age_section.append(lst[row][0].lower())
            row += 1
    #Creates a list of people in the same year
    years = []
    row = 0
    #Loops through the given list to find all available years
    while row < len(lst):
        if lst[row][2].lower() not in years:
            years.append(lst[row][2].lower())
        row += 1
    year_list = []
    #Loops through all of the available years and adds them to a list with \
    #people that are in that year
    for year in years:
        year_section = []
        year_list.append(year_section)
        year_section.append(year)
        row = 0
        while row < len(lst):
            if lst[row][2].lower() == year:
                year_section.append(lst[row][0].lower())
            row += 1
    #Creating the organized list -- adds the age list and year list as two \
    #elements
    return_list = [age_list, year_list]
    return return_list
#-------------------------------------------------------------------------------
def drawMe_five(n):
    """This function creates a nxn list (square list)"""
    #First row
    index = 2
    first_row_list = []
    first_row_list.append(".")
    first_row_list.append(".")
    while 1 < index < n - 1:
        first_row_list.append("*")
        index += 1
    first_row_list.append(".")
    #First block
    index = 2
    first_block_list = []
    first_block_list.append(".")
    first_block_list.append("*")
    while 0 < index < n:
        first_block_list.append(".")
        index += 1
    #Middle row / last row
    index = 1
    middle_bottom_row_list = []
    middle_bottom_row_list.append(".")
    while 0 < index < n - 2:
        middle_bottom_row_list.append("*")
        index += 1
    middle_bottom_row_list.append(".")
    middle_bottom_row_list.append(".")
    #Second block
    index = 0
    second_block_list = []
    while index < n - 2:
        second_block_list.append(".")
        index += 1
    second_block_list.append("*")
    second_block_list.append(".")
    #Creating the final list
    final_matrix = []
    #Adds the first row
    final_matrix.append(first_row_list)
    #Adds the first block
    final_matrix.append(first_block_list)
    for index in range(int((n - 5)/2)):
        final_matrix.append(first_block_list)
    #Adds the middle row
    final_matrix.append(middle_bottom_row_list)
    #Adds the second block
    final_matrix.append(second_block_list)
    for index in range(int((n - 5)/2)):
        final_matrix.append(second_block_list)
    #Adds the bottom row
    final_matrix.append(middle_bottom_row_list)
    return final_matrix
#-------------------------------------------------------------------------------
def find_Battleship(lst, guess):
    """This function returns a string stating whether a ship was hit"""
    #Checks if the guess is a hit
    if lst[guess[1]][guess[2]] == "X":
        #Checks horizontally for a Cruiser
        counter = 0
        #Checks every character in the given row
        if guess[2] < len(lst[guess[1]]) - 1:
            if lst[guess[1]][guess[2] + 1] == "X":
                counter += 1
        if 0 < guess[2]:
            if lst[guess[1]][guess[2] - 1] == "X":
                counter += 1
        #If there are more than 1 "X" in the row, it is a cruiser
        if counter > 0:
            if guess[0].lower() == "cruiser":
                return "it's a hit!"
            else:
                return "it's a hit, but not that ship"
        else:
            counter = 0
            index = 0
            #Checks every character in the given column
            if guess[1] < len(lst) - 1:
                if lst[guess[1] + 1][guess[2]] == "X":
                    counter += 1
            if 0 < guess[1]:
                if lst[guess[1] - 1][guess[2]] == "X":
                    counter += 1 
            #If there are more than 1 "X" in the column, it is a destroyer
            if counter > 0:
                if guess[0].lower() == "destroyer":
                    return "it's a hit!"
                else:
                    return "it's a hit, but not that ship"
            #Otherwise, it is a carrier
            else:
                if guess[0].lower() == "carrier":
                    return "it's a hit!"
                else:
                    return "it's a hit, but not that ship"    
    else:
        return "it's a miss!"