#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 10
# Due Date: 11/10/2020
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
def dams_by_state(inputfilename):
    """Transforms a file into a dictionary of data"""
    m_dict = dict()
    inputfile = open(inputfilename, "r")
    #Creates a list with each line of text an element
    lines = []
    for line in inputfile:
        lines.append(line)
    #Creating the header information
    headers = lines[0]
    headers_list = headers.split(",")
    headers_list.remove("Name")
    headers_list.remove("State")
    #Removing the newline from the "Year" element
    headers_list[-1] = headers_list[-1][:-1]
    #Loops through every line after the header line
    for line in range(len(lines) - 1):
        #Creates a list of current values for the headers
        current_line = lines[line + 1]
        current_list = current_line.split(",")
        #Removing the newline
        current_list[-1] = current_list[-1][:-1]
        #First Level
        state = current_list[8]
        current_list.remove(state)
        #Second Level
        s_dict = dict()
        name = current_list[3]
        current_list.remove(name)
        #Making the number-values integers and/or floats
        #Certain indexes in the current_list are number-values
        for index in range(len(current_list)): 
            #Converts the values to integers
            if (0 <= index <= 2) or (5 <= index <= 6):
                current_list[index] = float(current_list[index])
            #Converts the values to floats
            elif (index == 8):
                current_list[index] = int(current_list[index])
        #Third Level
        t_dict = dict()
        #Creates a dictionary for a specific dam within a state
        for index in range(len(headers_list)):
            t_dict[headers_list[index]] = current_list[index]
        #Checking to see if there are multiple entries for one state
        counter = 0
        for states in m_dict.keys():
            if state in m_dict.keys():
                counter += 1
        #Adding everything to the main dictionary
        #If the state has not already been added to the main dictionary, \
        #the state and its information is added to it
        if counter == 0:
            s_dict[name] = t_dict
            m_dict[state] = s_dict
        #If the state has already been added to the main dictionary, \
        #the state is updated with the new information
        else:
            s_dict[name] = t_dict
            m_dict[state].update(s_dict)
    return m_dict
#-------------------------------------------------------------------------------
def count_dams(inputfilename, state = "VA"):
    """Checks the amount of dams in a given state"""
    #creates a variable for an organized dictionary
    dams_dict = dams_by_state(inputfilename)
    counter = 0
    #If the state is in the file, the branch executes
    if state in dams_dict.keys():
        #Adds 1 to counter for every dam in a state
        for dam in dams_dict[state]:
            counter += 1
    return counter
#-------------------------------------------------------------------------------
def dams_in_area(inputfilename,x1,y1,x2,y2):
    """Returns a set of dam names that exist in a coordinate rectangle"""
    dam_rt = set()
    file_info = dams_by_state(inputfilename)
    #If true, the coordinates make a rectangle, and the branch executes
    if x1 < x2 and y1 < y2:
        #Checks every dam to see if it is within the rectangle
        for state in file_info:
            for dam in file_info[state]:
                if float(file_info[state][dam]["Longitude"]) > x1 and \
                float(file_info[state][dam]["Longitude"]) < x2:
                    if float(file_info[state][dam]["Latitude"]) > y1 and \
                    float(file_info[state][dam]["Latitude"]) < y2:
                        #If a dam is within the rectangle, it is added to the \
                        #set
                        dam_rt.add(dam)
        return dam_rt
    #If the coordinates do not form a rectangle, then the function returns none
    else:
        return dam_rt
#-------------------------------------------------------------------------------
def average_by_state(inputfilename):
    """Writes averages to a file"""
    #Creating the header information
    header = "State,AverageCrestElevation,AverageCrestLength,\
AverageStructuralHeight\n"
    #Finding relevant information and opening the file
    file_info = dams_by_state(inputfilename)
    file_output = "averages.csv"
    f = open(file_output, "w")
    #Writing the header
    f.write(header)
    other_lines = []
    #Loops through every state in the dictionary
    for state in file_info.keys():
        #Creates the variables for the averages
        avg_crest_e = float(0)
        avg_crest_l = float(0)
        avg_str = float(0)
        dams = file_info[state].keys()
        num_dams = len(dams)
        #The information from every dam in the state is summed to the \
        #average values variables 
        for dam in dams:
            avg_crest_e += float(file_info[state][dam]["CrestElevation"])
            avg_crest_l += float(file_info[state][dam]["CrestLength"])
            avg_str += float(file_info[state][dam]["StructuralHeight"])
        #The average variables are divided by num_dams to find the averages
        #They are then converted to strings
        avg_crest_e = str(round((avg_crest_e / num_dams), 1))
        avg_crest_l = str(round((avg_crest_l / num_dams), 1))
        avg_str = str(round((avg_str / num_dams), 1))
        #Adding lines to a list
        other_lines.append(state + "," + avg_crest_e + "," + avg_crest_l + \
        "," + avg_str + "\n")
    #Writing and sorting every line in the lines list
    other_lines.sort()
    for lin in other_lines:
        f.write(lin)
    f.close()