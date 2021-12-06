#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 9
# Due Date: 11/1/2020
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
def index(d):
    """Creates a dictionary with different keys and values"""
    d_new = {}
    num_vals = set()
    #Creates a set of all the numbers
    for list in d.values():
        for value in list:
            num_vals.add(value)
    #Checks every value in the original dictionary
    for num in num_vals:
        index = 0
        temp = set()
        #Checks every key in the original dictionary
        for key in d.keys():
            #If the value is in the specific key, the branch executes
            if num in d[key]:
                  temp.add(key)
            index += 1
        #Once all keys are found for one value, the value/key pairs are \
        #added as a new dictionary entry
        d_new[num] = temp
    return d_new
#-------------------------------------------------------------------------------
def merge(d1,d2):
    """Returns a dictionary that merges two wine inventories"""
    d_new = {}
    #Loops through all of the wine types in d1
    for key in d1.keys():
        #If the wine type is in d2, the branch executes
        if key in d2.keys():
            for key1 in d1[key].keys():
                #If the year in d1 is the same as d2, the values from both \
                #dictionaries are added together
                if key1 in d2[key].keys():
                    d2[key][key1] = d2[key][key1] + d1[key][key1]
                #If the year in d1 is different from d2, the year-value pair \
                #from d2 is assigned with the one from year one
                else:
                    d2[key][key1] = d1[key][key1]
    #Everything from d1 is copied over to the new dictionary
    d_new = d1
    #Everything from d2 is added and/or copied over to the new dictionary
    d_new.update(d2)
    return d_new
#-------------------------------------------------------------------------------
def popular_genre(d):
    """Returns a set with all of the movies related to the most popular genre"""
    genres = set()
    pref_genre = []
    r_movies = set()
    #Creates a set of all the genres
    for movie in d.keys():
        for genre in d[movie][1]:
            genres.add(genre)
    max_count = 0
    #Finds the most popular genres
    for genre in genres:
        count = 0
        for movie in d.keys():
            if genre in d[movie][1]:
                count += 1
        #If there are more occurences of the genre, it is replaced with \
        #as the most popular genre
        if count > max_count:
            pref_genre = []
            pref_genre.append(genre)
            max_count = count
        #If the amount of occurences of the genre is same as the most \
        #popular genre, it is added as s most popular genre
        elif count == max_count:
            pref_genre.append(genre)
    #Creates a set of movies that have the popular genres
    for movie in d.keys():
        for genre in pref_genre:
            #If the genre is in the movie, the movie is added to the set
            if genre in d[movie][1]:
                r_movies.add(movie)
    return r_movies
#-------------------------------------------------------------------------------
def subset(group, total):
    """Creates the smallest subset of group that has a larger sum than total"""
    #If group is empty, it returns False
    if group == set():
        return False
    group_sum = 0
    #Calculates the sum of all numbers in group
    for num in group:
        group_sum += num
    max_sum = 0
    num_set = set()
    #If the sum of the group is greater than the total value, the branch executes
    if group_sum > total:
        num_set_sum = 0
        #Runs while the sum of all numbers in the set is not greater than the \
        #total value
        while num_set_sum <= total:
            #Finds the maximum value in the group
            for num in group:
                max_num = 0
                if num not in num_set and num > max_num:
                    max_num = num     
            #Adds the maximum value to the set and removes it from the group
            num_set.add(max_num)
            group.remove(num)
            #Adds the number to the set sum
            num_set_sum += max_num
        return num_set
    #If the sum of the group is less than the total value, it returns False
    else:
        return False
#-------------------------------------------------------------------------------
def capitalization(d):
    """Capitalizes the first character of every string within a dictionary"""
    d_keys = []
    #Creates a list of the keys in d
    for key in d.keys():
        d_keys.append(key)
    #Capitalizes all key strings if they are lowercase
    for key in range(len(d_keys)):
        name = ""
        num = 97
        #Checks every lowercase character for equality
        while num < 123:
            #If true, an uppercase letter is added to name followed by the \
            #rest of the characters from the original string
            #The original string is removed and name is added
            if ord(d_keys[key][0]) == ord(chr(num)):
                name += chr(num - 32)
                name += d_keys[key][1:]
                d[name] = d[d_keys[key]]
                del d[d_keys[key]]
                num = 123
            else:
                num += 1
    d_values = []
    #Creates a list of the values in d
    for value in d.values():
        d_values.append(value)
    #Capitalizes all the value strings if they are lowercase
    for key,value in d.items():
        for val in range(len(value)):
            name = ""
            character = 97
            #Checks every lowercase character for equality
            while character < 123:
                #If true, an uppercase letter is added to name followed by the \
                #rest of the characters from the original string
                #The original string is replaced with name
                if ord(d[key][val][0]) == ord(chr(character)):
                    name += chr(character - 32)
                    name += d[key][val][1:]
                    d[key][val] = name
                    character = 123
                else:
                    character += 1
    return d