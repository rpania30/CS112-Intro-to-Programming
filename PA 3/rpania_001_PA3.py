#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 3
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
#LISTS

#point values for the moves of every fighter type (earth, fire, water, air)
#five points
five_point_moves = ["rock bullets", "fire shield", "water wave", "air ball"]
#ten points
ten_point_moves = ["dust devil", "fly kick", "waterspout", "air blast"]
#fifteen points
fifteen_point_moves = ["earth armor", "swing kick", "ice spears", "air bomb"]
#twenty points
twenty_point_moves = ["earth levitation", "fire fly", "freeze", "air funnel"]
#twenty five points
twentyfive_point_moves = ["tectonics", "fireball", "waterburst", "air punch"]

#move names
#earth
earth_names = ["rock bullets", "dust devil", "earth armor", \
    "earth levitation", "tectonics"]
#fire
fire_names = ["fire shield", "fly kick", "swing kick", "fire fly", "fireball"]
#water
water_names = ["water wave", "waterspout", "ice spears", \
    "freeze", "waterburst"]
#air
air_names = ["air ball", "air blast", "air bomb", "air funnel", "air punch"]

#-------------------------------------------------------------------------------
#Function determines a player's type based on the move they made
#The fuction checks the names lists for the particular move given
def whatType(moveName):
    if moveName in earth_names:
        playerType = "earth"
        return playerType
    elif moveName in fire_names:
        playerType = "fire"
        return playerType
    elif moveName in water_names:
        playerType = "water"
        return playerType
    else:
        playerType = "air"
        return playerType

#-------------------------------------------------------------------------------
#Function outputs the point category a particular move is in
#Function checks the points lists for the particular move given using the \
#"in" operator
def calcPoints(moveName):
    if moveName in five_point_moves:
        points = 5
        return points
    elif moveName in ten_point_moves:
        points = 10
        return points
    elif moveName in fifteen_point_moves:
        points = 15
        return points
    elif moveName in twenty_point_moves:
        points = 20
        return points
    else:
        points = 25
        return points

#-------------------------------------------------------------------------------
#After a single move, this function determines the winner out of 2 players
#With the point calculation from the past function, the location gives \
#the differing point values with each location
#Once a points value is found for player 1 and 2, the values are compared and \
#the winner is returned
def whoWins(p1Move, p2Move, location):
    p1points = calcPoints(p1Move)
    p2points = calcPoints(p2Move)
    if location == "full moon bay":
        if whatType(p1Move) == "earth":
            p1points += 5
        elif whatType(p1Move) == "fire":
            p1points -= 1
        elif whatType(p1Move) == "water":
            p1points += 3
        else:
            p1points -= 2
        if whatType(p2Move) == "earth":
            p2points += 5
        elif whatType(p2Move) == "fire":
            p2points -= 1
        elif whatType(p2Move) == "water":
            p2points += 3
        else:
            p2points -= 2
    elif location == "beach cave":
        if whatType(p1Move) == "earth":
            p1points -= 2
        elif whatType(p1Move) == "fire":
            p1points += 5
        elif whatType(p1Move) == "water":
            p1points -= 1
        else:
            p1points += 3
        if whatType(p2Move) == "earth":
            p2points -= 2
        elif whatType(p2Move) == "fire":
            p2points += 5
        elif whatType(p2Move) == "water":
            p2points -= 1
        else:
            p2points += 3
    elif location == "foggy swamp":
        if whatType(p1Move) == "earth":
            p1points += 3
        elif whatType(p1Move) == "fire":
            p1points -= 2
        elif whatType(p1Move) == "water":
            p1points += 5
        else:
            p1points -= 1
        if whatType(p2Move) == "earth":
            p2points += 3
        elif whatType(p2Move) == "fire":
            p2points -= 2
        elif whatType(p2Move) == "water":
            p2points += 5
        else:
            p2points -= 1
    else:
        if whatType(p1Move) == "earth":
            p1points -= 1
        elif whatType(p1Move) == "fire":
            p1points += 3
        elif whatType(p1Move) == "water":
            p1points -= 2
        else:
            p1points += 5
        if whatType(p2Move) == "earth":
            p2points -= 1
        elif whatType(p2Move) == "fire":
            p2points += 3
        elif whatType(p2Move) == "water":
            p2points -= 2
        else:
            p2points += 5
    if p1points > p2points:
        winner = "player 1 wins!"
        return winner
    elif p2points > p1points:
        winner = "player 2 wins!"
        return winner
    else:
        winner = "it's a tie!"
        return winner

#-------------------------------------------------------------------------------
#Determines if a player has an advantage at certain locations based on types
#The == operator helps the function compare the given location with locations \
#inside the function, as well as the given player type with the player types
def hasAdvantage(playerType, location):
    if location == "full moon bay":
        if playerType == "earth":
            result = "has great advantage"
            return result
        elif playerType == "fire":
            result = "no advantage"
            return result
        elif playerType == "water":
            result = "has some advantage"
            return result
        else:
            result = "no advantage"
            return result
    elif location == "beach cave":
        if playerType == "earth":
            result = "no advantage"
            return result
        elif playerType == "fire":
            result = "has great advantage"
            return result
        elif playerType == "water":
            result = "no advantage"
            return result
        else:
            result = "has some advantage"
            return result
    elif location == "foggy swamp":
        if playerType == "earth":
            result = "has some advantage"
            return result
        elif playerType == "fire":
            result = "no advantage"
            return result
        elif playerType == "water":
            result = "has great advantage"
            return result
        else:
            result = "no advantage"
            return result
    else:
        if playerType == "earth":
            result = "no advantage"
            return result
        elif playerType == "fire":
            result = "has some advantage"
            return result
        elif playerType == "water":
            result = "no advantage"
            return result
        else:
            result = "has great advantage"
            return result

#-------------------------------------------------------------------------------
#Calculates total points after a 3 move combo made by one player
#Since there is only one player, the type of one move will give the type \
#of the player
#The program checks each location for how they will effect the point values \
#of the combo
#The advantages/disadvantages are tripled for the 3 moves
def countMyCombo(move1, move2, move3, location):
    combo_points = calcPoints(move1) + calcPoints(move2) + calcPoints(move3)
    if location == "full moon bay":
        if whatType(move1) == "earth":
            total = combo_points + 15
            return total
        elif whatType(move1) == "fire":
            total = combo_points - 3
            return total
        elif whatType(move1) == "water":
            total = combo_points + 9
            return total
        else:
            total = combo_points - 6
            return total
    elif location == "beach cave":
        if whatType(move1) == "earth":
            total = combo_points - 6
            return total
        elif whatType(move1) == "fire":
            total = combo_points + 15
            return total
        elif whatType(move1) == "water":
            total = combo_points - 3
            return total
        else:
            total = combo_points + 9
            return total
    elif location == "foggy swamp":
        if whatType(move1) == "earth":
            total = combo_points + 9
            return total
        elif whatType(move1) == "fire":
            total = combo_points - 6
            return total
        elif whatType(move1) == "water":
            total = combo_points + 15
            return total
        else:
            total = combo_points - 3
            return total
    else:
        if whatType(move1) == "earth":
            total = combo_points - 3
            return total
        elif whatType(move1) == "fire":
            total = combo_points + 9
            return total
        elif whatType(move1) == "water":
            total = combo_points - 6
            return total
        else:
            total = combo_points + 15
            return total   