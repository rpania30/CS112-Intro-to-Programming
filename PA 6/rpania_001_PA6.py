#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 6
# Due Date: 10/11/2020
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
#Function creates a string based on the provided list. Each number in the list \
#specifies how many characters from the string that follows belong in the \
#resulting string.
def mashup(lst):
    endstr = ""
    index = 0
    #Loops through every pair in the list
    while index < len(lst):
        #Resets index2 everytime the outer loop is run
        index2 = 0
        #If the number is greater than the string, the pair is skipped
        if lst[index] > len(lst[index + 1]):
            index += 2
        #If the string is empty, the pair is skipped
        elif lst[index + 1] == "":
            index += 2
        else:
            #Loops through a given amount of times (the number in the pair)
            for x in range(lst[index]):
                #Adds a character to the output string
                endstr += lst[index + 1][index2]
                index2 += 1
            index += 2
    return endstr
#-------------------------------------------------------------------------------
#Function returns the given list of numbers that has been expanded with a \
#certain amount of zeroes around all of the numbers, including at the beginning\
# and end of the list. 
def expand(numbers, amount):
    index = 0 
    #Loops though every number in the list
    while index <= len(numbers):
        #Loops through every number in the range of amount
        for x in range(amount):
            #inserts a 0 at the given index
            numbers.insert(index, 0)
        index += amount + 1
    #Nothing is returned (elements are added/rearranged in the list)
#-------------------------------------------------------------------------------
#Function determines the size of the largest square that can be made with the \
#given matrix. It then constructs a new square matrix of this size using the \
#elements from the original matrix in their original order. 
def squarify(matrix):
    n_mtrx = []
    row_max = 0
    #Loop determines how many rows there are in the list
    for row in range(len(matrix)):
        row_max += 1
    #Loop determines how many colimns are in the list
    for row in matrix:
        column_max = 0
        for column in row:
            column_max += 1
    #If the amount of rows is greater than the amount of columns, the amount \
    #of rows is decreased incrementally until they are equal
    if row_max > column_max:
        while row_max > column_max:
            row_max -= 1
    #If the amount of columns is greater than the amount of rows, the amount \
    #of columns is decreased incrementally until they are equal
    elif column_max > row_max:
        while column_max > row_max:
            column_max -= 1
    #Loop adds elements from the given list into the new list (once the \
    #maximum amount of columns and rows is determined.
    for row in range(row_max):
        #row_box creates rows within the new list, n_mtrx
        row_box = []
        n_mtrx.append(row_box)
        #Loop adds elements from rows in matrix to rows in n_mtrx
        for column in range(column_max):
            row_box.append(matrix[row][column])
    return n_mtrx
#-------------------------------------------------------------------------------
#Function adds each pair of numbers that are overlapped with the mask, and \
#updates the original matrix with a new value. The mask shifts down the row to \
#the next 2 values. Once two rows are looped over, it shifts to the next two \
#rows. If the mask overlaps over an edge, ignore the portion over the edge \
#and go to the next two rows 
def apply(mask, matrix):
    for row in range(len(matrix)):
        #If the row is even, loops through the first while loop
        if row % 2 == 0:
            column = 0
            #Loops through every other element in the row
            while column < len(matrix[row]):
                #If the element is the last one in the row, adds a number \
                #to that element, then ends the loop
                if column == len(matrix[row]) - 1:
                    matrix[row][column] += mask[0][0]
                    column += 1
                else:
                    matrix[row][column] += mask[0][0]
                    matrix[row][column + 1] += mask[0][1]
                    column += 2
        #If the row is odd, loops through the second while loop
        elif row % 2 == 1:
            column = 0
            #Loops through every other element in the row
            while column < len(matrix[row]):
                #If the element is the last one in the row, adds a number \
                #to that element, then ends the loop
                if column == len(matrix[row]) - 1:
                    matrix[row][column] += mask[1][0]
                    column += 1
                else:
                    matrix[row][column] += mask[1][0]
                    matrix[row][column + 1] += mask[1][1]
                    column += 2
    #nothing is returned (elements are changed within the list itself)