#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 8
# Due Date: 9/25/2020
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
def clearable(locations, report_location):
    """Checks whether a player can be cleared from a murder"""
    cleared = []
    not_cleared = []
    #Checks locations for the report location
    for index in range(len(locations)):
        if locations[index] == report_location:
           not_cleared.append(locations[index])
        else:
            cleared.append(locations[index])
    #If the player was cleared more than they were not cleared, the player \
    #can be cleared
    if len(cleared) > len(not_cleared):
        return True
    else:
        return False
#-------------------------------------------------------------------------------
def get_sightings(location_log, player):
    """Constructs a list of all locations where player has been sighted"""
    location_seen = []
    #Checks if a person seen was the player desired
    for tuple in range(len(location_log)):
        #If the player in the tuple is the player desired, the location where \
        #they were seen is added to a list
        if location_log[tuple][1] == player:
            location_seen.append(location_log[tuple][2])
    #The list is returned
    return location_seen
#-------------------------------------------------------------------------------
def likely_imposters(report_location, players, location_log):
    """Constructs a list of all players who cannot be cleared of the murder"""
    likely_imp_lst = []
    #Loops through all players and adds players if they are not cleared \
    #for the specific locations
    for player in players:
        if clearable(get_sightings(location_log, player), report_location) \
        == False:
            likely_imp_lst.append(player)
    #The list is returned
    return likely_imp_lst
#-------------------------------------------------------------------------------
def task_filter(task_log, status = None, task_type = None, *ignored_names):
    """Constructs a list of task names based on its status and type"""
    task_names = []
    #Compares the desired task types and status for tasks
    for index in range(len(task_log)):
        #If there are inputs for task_type and status, certain tasks are \
        #added to a list, given the ignored_names
        if status != None and task_type != None:
            if task_log[index][1] == status and task_log[index][2] == task_type:
                if task_log[index][0] not in ignored_names:
                    task_names.append(task_log[index][0])
        #If there are inputs for status but not task type, certain tasks are \
        #added to a list
        elif task_type == None:
            if task_log[index][1] == status:
                task_names.append(task_log[index][0])
        #If there are inputs for task_type but not status, certain tasks are \
        #added to a list
        elif status == None:
            if task_log[index][2] == task_type:
                task_names.append(task_log[index][0])
        #If there are no inputs for task_type and status, every task is \
        #added to the lsit
        else:
            task_names.append(task_log[index][0])
    return task_names
#-------------------------------------------------------------------------------
def check_common(task_log_A, task_log_B):
    """Compares two different player task logs to check for same common tasks"""
    #Creates a list of common tasks for player A
    player_A = task_filter(task_log_A, task_type = True)
    #Creates a list of common tasks for player B
    player_B = task_filter(task_log_B, task_type = True)
    count = 0
    #Compares every task in player A's common tasks to player B's
    for player in player_A:
        if player in player_B:
            count += 1
    #If the two players have the same tasks, True is returned
    if count == len(player_B) and len(player_A) == len(player_B):
        return True
    #If the two players have different tasks, False is returned
    else:
        return False