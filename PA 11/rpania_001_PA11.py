#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 11
# Due Date: 11/17/2020
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
def print_num_pattern(num1, num2):
    """Creates an incremental list"""
    #The list starts with num1
    finList = [num1]
    #The function runs until the most recent value of finList is read as \
    #negative
    def before_app_list(currentVal, increment):
        #If the most recent element in finList is <= 0, the branch executes
        if finList[-1] <= 0:
            currentVal = finList[-1] + increment
            finList.append(currentVal)
            #The other helper function is referenced so that the element \
            #values in finList can climb back up to num1
            after_app_list(currentVal, increment)
        #If the most recent element in finList is a non-zero positive \
        #number, the branch executes
        else:
            currentVal = finList[-1] - increment
            finList.append(currentVal)
            #The helper function is called again
            before_app_list(currentVal, increment)
    #The function runs until 
    def after_app_list(currentVal, increment):
        #If the most recent element in finList is not equivalent to num1, \
        #the branch executes
        if finList[-1] != num1:
            currentVal = finList[-1] + increment
            finList.append(currentVal)
            #The helper function is called again until the final element in \
            #finList is 
            after_app_list(currentVal, increment)
    #The first helper function is called to start the recursions
    before_app_list(num1, num2)
    return finList
#-------------------------------------------------------------------------------
def count_multiples(num1, num2, N):
    """Calculates the number of multiples of N that exist within two values"""
    numMult = []
    def app_list(currentVal, final, multiple):
        #If currentVal is a multiple of multiple, the branch executes
        if currentVal % multiple == 0:
            numMult.append(currentVal)
        #If starting value is less than the final value, the branch executes
        if currentVal < final:
            #If the next value is between num1 and num2, the helper function \
            #is called with the next currentVal value
            if currentVal + 1 <= final:
                app_list(currentVal + 1, final, multiple)
        #If starting value is less than the final value, the branch executes
        else:
            #If the next value is between num1 and num2, the helper function \
            #is called with the next currentVal value
            if currentVal - 1 >= final:
                app_list(currentVal - 1, final, multiple)
    #The helper function is called to start the recursions
    app_list(num1, num2, N)
    #Because all multiples are added to a list, the length of the list can \
    #be used to find the number of existing multiples
    return len(numMult)
#-------------------------------------------------------------------------------
def scrabble_number(lst):
    """Creates scrabbled version of a list"""
    scrabList = []
    def swap_list_odd(lst, index1 = 1):
        #If the length of scrabList is 2 less than the length of lst, two \
        #elements can be swapped
        if len(scrabList) + 1 < len(lst):
            #The second element in a pair is added to scrabList
            scrabList.append(lst[index1])
            swap_list_even(lst, index1 - 1)
        #If the length of scrabList is 1 less than the length of lst, no \
        #elements can be swapped and the recursion ends
        elif len(scrabList) < len(lst):
            #The final element is added to scrabList
            scrabList.append(lst[index1 - 1])
    def swap_list_even(lst, index2):
        #The first element in a pair is added to scrabList
        scrabList.append(lst[index2])
        swap_list_odd(lst, index2 + 3)
    #The first helper function is called to start the recursions
    swap_list_odd(lst)
    return scrabList
#-------------------------------------------------------------------------------
def count_moves(start, end, step):
    """Counts the amount of moves to get from start to end by step"""
    posList = []
    #Adds every nextVal to posList
    def app_count(currentVal, fin, increment):
        #If the current value is less than end, the branch executes
        if currentVal < fin:
            #The next value is calculated, then added to posList
            nextVal = currentVal + increment
            posList.append(nextVal)
            #The step/increment is increased or left unchanged based off of \
            #the ending number of currentVal
            #In each branch, the helper function is recursed
            if str(currentVal)[-1] == str(3):
                increment += 3
                app_count(currentVal + increment, fin, increment)
            elif str(currentVal)[-1] == str(5):
                increment += 5
                app_count(currentVal + increment, fin, increment)
            elif str(currentVal)[-1] == str(7):
                increment += 7
                app_count(currentVal + increment, fin, increment)
            elif str(currentVal)[-1] == str(8):
                increment += 8
                app_count(currentVal + increment, fin, increment)
            else:
                app_count(currentVal + increment, fin, increment)
    #The helper function is called to start the recursions
    app_count(start, end, step)
    #The length of posList represents the number of steps taken to end
    return len(posList)
#-------------------------------------------------------------------------------
def removeLetter(word, char):
    """Removes all occurances of a letter from a word"""
    finLet = []
    #Adds every letter in word that is not char to finLet
    def app_word(ogStr, chr, index = 0):
        #If it is not the final letter in ogStr, the branch executes
        if index + 1 < len(ogStr):
            #If the letter is not char, the letter is added to finLet
            if ogStr[index] != chr:
                finLet.append(ogStr[index])
            #The function is called again with the next index value
            app_word(ogStr, chr, index + 1)
        #If it is the final letter in ogStr, the branch executes
        elif index < len(ogStr):
            #If the letter is not char, the letter is added to finLet
            if ogStr[index] != chr:
                finLet.append(ogStr[index])
    #The helper function is called to start the recursions
    app_word(word, char)
    #Each element in finLet is joined together in a new string, finWord
    finWord = "".join(finLet)
    return finWord