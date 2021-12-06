#-------------------------------------------------------------------------------
# Name: Rishi Pania
# Assignment 1
# Due Date: 9/6/20
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

pi = 3.14159

print("Welcome to CS 112")
# Welcomes user to CS 112

name = ""
name = input("What's your name? ")
# Asks user what their name is

current_time_input = input("What is the time in seconds? ")
# Asks user how long it has been since 12am in seconds

current_time_seconds = int(current_time_input) % 60
current_time_minutes = int(current_time_input) // 60
current_time_minutes_rmdr = current_time_minutes % 60
current_time_hours = current_time_minutes // 60
current_time = ("The time is " + str(current_time_hours) + "h " + str(current_time_minutes_rmdr) + "m " + str(current_time_seconds) + "s")
print(current_time)
# Prints time in hours, minutes, seconds form

def calculate_angle(hour, minute, second):
    second_angle = second / 60 * 360
    minute_angle = (minute + (second/60)) / 60 * 360
    hour_angle = (hour + (minute/60) + (second/3600)) / 12 * 360
    second_radian = second_angle * (pi/180)
    minute_radian = minute_angle * (pi/180)
    hour_radian = hour_angle * (pi/180)
    return second_angle, minute_angle, hour_angle, second_radian, minute_radian, hour_radian

second_degrees, minute_degrees, hour_degrees, second_radians, minute_radians, hour_radians = calculate_angle(current_time_hours, current_time_minutes_rmdr, current_time_seconds)

print("The angles of the three hands are " + str(round(hour_degrees, 5)), str(round(minute_degrees, 5)), str(int(second_degrees)) + " degrees or " + str(round(hour_radians, 5)), str(round(minute_radians, 5)), str(round(second_radians, 5)) + " radians")
# Lists the angles of each hand from 12am (in degrees and radians)

def calculate_angle_between(hour, minute):
    a = max(hour, minute)
    b = min(hour, minute)
    angle_between_degree1 = abs(a - b)
    angle_between_degree2 = 360 - abs(a - b)
    angle_between_degree = min(angle_between_degree1, angle_between_degree2)
    angle_between_radian = angle_between_degree * (pi/180)
    return angle_between_degree, angle_between_radian
    
angle_between_degrees, angle_between_radians = calculate_angle_between(hour_degrees, minute_degrees)

print("The angle between the hour hand and the minutes hand is " + str(round(angle_between_degrees, 5)) + " degrees or " + str(round(angle_between_radians, 5)) + " radians") 
# Lists the angle between the hour hand and minutes hand

clock_diameter = float(input("What is the diameter of the clock in inches? "))
# Asks user what the diameter of the clock is

def calculate_area_sector(angle, diameter):
    area_sector_inch = (angle/360) * pi * (diameter / 2) ** 2
    area_sector_meter = (angle/360) * pi * ((diameter * 0.0254) / 2) ** 2
    return area_sector_inch, area_sector_meter

area_sector_inches, area_sector_meters = calculate_area_sector(angle_between_degrees, clock_diameter)

print("The area of the slice between the hour hand and the minutes hand is " + str(round(area_sector_inches, 5)) + " sq. inches or " + str(round(area_sector_meters, 5)) + " sq. meters")
# Lists the area of the slice between the hour and minutes hands

clock_diameter_new = float(input("What is the new diameter of the clock in inches? "))
# Asks user what the new diameter of the clock is

def calculate_new_angle_sector(area, diameter):
    new_angle_degree = (360 * area) / (((diameter/2)** 2) * pi)
    new_angle_radian = new_angle_degree * (pi/180)
    return new_angle_degree, new_angle_radian

new_angle_degrees, new_angle_radians = calculate_new_angle_sector(area_sector_inches, clock_diameter_new)

print("The new angle between the hour hand and the minutes hand must be " + str(round(new_angle_degrees, 5)) + " degrees or " + str(round(new_angle_radians, 5)) + " radians")
# Lists the new angle between the hour and minutes hand

print("Have a good day", name + "!")
# Wishes the user has a good day