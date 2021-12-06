#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 12
# Due Date: 11/24/2020
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
class Phone:
    def __init__(self, name, area_code, number, is_active = True):
        """Constructs a telephone line and creates instance variables"""
        self.name = name
        self.area_code = area_code
        self.number = number
        self.is_active = is_active
    def __str__(self):
        """Creates and returns string"""
        rstr = str(self.area_code) + "-" + str(self.number)[:3] + "-" + \
        str(self.number)[3:] + " (" + self.name + ")"
        return rstr
    def __repr__(self):
        return self.__str__()
    def __eq__(self, compare):
        """Determines if an object is equivalent to another"""
        #Compares the area codes and numbers of the two objects
        if self.area_code == compare.area_code and \
        self.number == compare.number:
            return True
        else:
            return False
    def activate(self):
        """Activates a phone line"""
        self.is_active = True
    def deactivate(self):
        """Deactivates a phone line"""
        self.is_active = False
#-------------------------------------------------------------------------------
class Call:
    def __init__(self, caller, callee, length):
        """Constructs a telephone line and creates instance variables"""
        #Checks if the phone lines are both active
        if caller.is_active == True and callee.is_active == True:
            #Checks if the caller and callee are the same phone line
            if caller != callee:
                #Checks if the length of the phone call is greater than 0
                if length >= 0:
                    self.caller = caller
                    self.callee = callee
                    self.length = length
    def __str__(self):
        """Creates and returns string"""
        rstr = "Call: " + self.caller.__repr__() + " -> " + \
        self.callee.__repr__() + " | " + str(self.length)
        return rstr
    def __repr__(self):
        return self.__str__()
    def is_local(self):
        """Determines whether a phone call is local or not"""
        #Compares the area codes of the caller and callee
        if self.caller.area_code == self.callee.area_code:
            return True
        else:
            return False
#-------------------------------------------------------------------------------
class Features:
    def __init__(self, basic_rate, default_mins, rate_per_min, has_rollover):
        """Constructs a set of features and creates instance variables"""
        self.basic_rate = basic_rate
        self.default_mins = default_mins
        self.rate_per_min = rate_per_min
        self.has_rollover = has_rollover
    def __str__(self):
        """Creates and returns string"""
        rstr = "Basic rate: " + str("{:.2f}".format(self.basic_rate)) + \
        ", Default mins: " + str(self.default_mins) + ", Rate/min: " + \
        str("{:.2f}".format(self.rate_per_min)) + ", Rollover: " + \
        str(self.has_rollover)
        return rstr
    def __repr__(self):
        return self.__str__()
#-------------------------------------------------------------------------------
class Plan:
    def __init__(self, features, phones = []):
        """Constructs a phone plan and creates instance variables"""
        self.features = features
        self.phones = phones
        self.calls = []
        self.balance = 0
        self.rollover_mins = 0
        self.mins_to_pay = 0
    def __str__(self):
        """Creates and returns string"""
        rstr = "Plan (" + self.features.__repr__() + ", " + \
        self.phones.__repr__() + ", " + self.calls.__repr__() + ")"
        return rstr
    def add_call(self, call):
        #Checks whether the caller or callee of the call is in the self.phones
        if call.caller in self.phones or call.callee in self.phones:
            x = self.calls
            #Adds the call to self.calls
            x.append(call)
            #Checks whether a call is local by comparing area codes of the \
            #caller and callee
            if call.is_local() == False:
                #Checks if either the caller or callee of a call is in \
                #self.phones
                if call.caller not in self.phones or call.callee not in \
                self.phones:
                    #Adds the length of the call to self.mins_to_pay
                    self.mins_to_pay += call.length
            return None
        else:
            return False
    def remove_call(self, call):
        #Checks if a call is in self.calls
        if call in self.calls:
            #Removes a given call from self.calls
            self.calls.remove(call)
            return None
        else:
            return False
    def make_call(self, caller, callee, length):
        #If the length is less than 0, then return False
        if length < 0:
            return False
        #Creates an instance of Call with the function's parameters
        vcall = Call(caller, callee, length)
        #Checks if caller and callee of vcall are active
        if vcall.caller.is_active == True and vcall.callee.is_active == True:
            #Checks whether caller and callee of vcall are the same phone line
            if vcall.caller != vcall.callee:
                #Checks whether the phone call length of vcall is greater \
                #than 0
                if vcall.length >= 0:
                    #Calls add_call using the vcall instance
                    self.add_call(vcall)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def mins_by_phone(self, phone):
        #Loops through all of the calls in self.calls
        for call in self.calls:
            #Checks if the caller of a call is equivalent to the phone
            if phone.__eq__(call.caller) == True:
                #self.mins_to_pay is incremented by the length of a call
                self.mins_to_pay += call.length
            #Checks if the callee of a call is equivalent to the phone
            elif phone.__eq__(call.callee) == True:
                #self.mins_to_pay is incremented by the length of a call
                self.mins_to_pay += call.length
        return self.mins_to_pay
    def add_phone(self, phone):
        #Loops through every phone line in self.phones
        for element in self.phones:
            #Checks if a phone line is the same as the given phone line
            if phone.__eq__(element) == True:
                return False
            else:
                #Adds the given phone line to self.phones
                self.phones.append(phone)
        return None
    def remove_phone(self, phone):
        #Creates a new list
        nlst = []
        #Checks whether a given phone line is in self.phones
        if phone in self.phones:
            #Removes the given phone line from self.phones
            self.phones.remove(phone)
            #Loops through every call in self.calls
            for call in self.calls:
                #Checks if the caller and callee of a call are the same as \
                #the given phone line
                if phone != call.caller and phone != call.callee:
                    #Adds a call to the new list
                    nlst.append(call)
                elif call.caller in self.phones or call.callee in self.phones:
                    #Adds a call to nlst
                    nlst.append(call)
            #Sets self.calls equal to nlst
            self.calls = nlst
            return None
        else:
            return False
    def billing(self):
        #Checks whether the default_mins is less than the mins_to_pay
        if self.mins_to_pay <= self.features.default_mins:
            #Checks whether the plan uses rollover mins
            if self.features.has_rollover == True:
                #Adds to rollover_mins
                self.rollover_mins += (self.features.default_mins \
                - self.mins_to_pay)
                #Adds the basic rate to the final balance
                self.balance += self.features.basic_rate
            else:
                #Adds the basic rate to the final balance
                self.balance += self.features.basic_rate
        else:
            #Checks whether a plan uses rollover mins
            if self.features.has_rollover == True:
                #Checks whether the default_mins is greater than the \
                #mins_to_pay with rollover_mins
                if self.mins_to_pay <= self.features.default_mins + \
                self.rollover_mins:
                    #Adds the leftover rollover mins to self.rollover_mins
                    self.rollover_mins += self.features.default_mins - \
                    self.mins_to_pay
                    #Adds the basic rate to the final balance
                    self.balance += self.features.basic_rate
                else:
                    #Decreases self.mins_to_pay by the rollover mins used
                    self.mins_to_pay -= self.rollover_mins
                    #Adds the basic rate, but also the rate_per_min costs to \
                    #self.balance
                    self.balance += (self.features.basic_rate + \
                    (self.features.rate_per_min * (self.mins_to_pay - \
                    self.features.default_mins)))
            else:
                #Adds the basic rate, but also the rate_per_min costs to \
                #self.balance
                self.balance += (self.features.basic_rate + \
                (self.features.rate_per_min * (self.mins_to_pay - \
                self.features.default_mins)))
        #Loops through every call in self.calls
        for call in self.calls:
            #Removes call from self.calls
            self.calls.remove(call)
        #Checks whether the final balance is greater than 5 times the \
        #basic rate
        if self.balance > (self.features.basic_rate * 5):
            #Loops through every line in self.phones
            for line in self.phones:
                #Deactivates line
                line.deactivate()
        #Sets self.mins_to_pay back to 0
        self.mins_to_pay = 0
        return None