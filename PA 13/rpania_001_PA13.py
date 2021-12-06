#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 13
# Due Date: 12/06/2020
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
class Plane:
    def __init__(self, model, manufacturer, fuel):
        """Constructs a plane and creates instance variables"""
        self.model = model
        self.manufacturer = manufacturer
        #Checks if the fuel is a valid amount
        if fuel > 100.0 or fuel < 0.0:
            raise PlaneError("bad fuel " + str(fuel))
        else:
            self.fuel = fuel
    def __str__(self):
        """Creates and returns a string"""
        rstr = str(self.model) + ", " + str(self.manufacturer) + " :: " + \
        str(self.fuel) + " / 100"
        return rstr
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        """Determines if a plane is equivalent to another"""
        if self.model == other.model and self.manufacturer == \
        other.manufacturer:
            return True
        else:
            return False
    def is_empty(self):
        """Determines whether a plane's fuel is empty"""
        if self.fuel == 0:
            return True
        else:
            return False
    def refuel(self, amount):
        """Determines whether a plane can be refueled by amount"""
        #Checks if the amount is valid, or if the amount will be overcapacity
        if amount < 0 or self.fuel + amount > 100:
            raise PlaneError("unable to refuel by " + str(amount))
        else:
            self.fuel += amount
class Hangar:
    def __init__(self, name):
        """Constructs a plane hangar and creates instance variables"""
        self.name = name
        self.planes = []
    def __str__(self):
        """Creates and returns a string"""
        rstr = str(self.name) + ":\n"
        #Adds to the string for every plane in self.planes
        for i in range(len(self.planes)):
            vtemp = self.planes[i]
            rstr += "\t" + vtemp.__repr__() + "\n"
        return rstr
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        """Determines if a list of planes is equivalent to another"""
        #Checks to see if the two lists are the same length
        if len(self.planes) == len(other.planes):
            index = 0
            #Loops through every plane in both lists and compares them
            while index < len(other.planes):
                #If one of the elements are not equal to the other, \
                #False is returned
                if self.planes[index] != other.planes[index]:
                    return False
                index += 1
            return True
        else:
            return False
    def add_plane(self, plane):
        """Adds a plane to a list of planes"""
        #Checks if plane is in self.planes
        if plane in self.planes:
            raise PlaneError("duplicate plane '" + str(plane.model) + ":" + \
            str(plane.manufacturer) + "'")
        else:
            #Adds a plane to the list
            self.planes.append(plane)
    def plane_by_model(self, model):
        """Finds a plane object with a specific model"""
        #Loops through every plane in self.planes
        for i in self.planes:
            #Checks whether the plane model is the same as model
            if i.model == model:
                return i
        raise PlaneError("no plane found with model '" + str(model) + "'")
    def planes_by_manufacturer(self, company):
        """Creates a list of planes that were built by a manufacturer"""
        nlst = []
        #Loops through every plane in self.planes
        for i in self.planes:
            #Checks whether the plane manufacturer is the same as company
            if i.manufacturer == company:
                nlst.append(i)
        #Checks if the length of the list is greater than 0
        if len(nlst) > 0:
            return nlst
        else:
            raise PlaneError("no planes built by '" + str(company) + "'")
    def total_empty(self):
        """Determines the number of planes that are out of fuel in a list"""
        count = 0
        #Loops through every plane in self.planes
        for i in self.planes:
            #Checks if the plane fuel is empty
            if i.is_empty() == True:
                count += 1
        return count
    def refuel_all(self, amount):
        """Refuels all planes in a hangar by amount"""
        #Loops through every plane in planes
        for i in self.planes:
            #Attempts to refuel the plane
            try:
                i.refuel(amount)
            except:
                continue
class PlaneError(Exception):
    def __init__(self,msg):
        """Constructs message instance variable"""
        self.msg = msg
    def __str__(self):
        """Creates and returns an error message"""
        return self.msg