# David Powis-Dow CS 101:Python 
# 2016-1-21 v0.1
# Chapter 6 : Exercise 5 - Day_Add with negative deltas

import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno        # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

    
def test_suite():
    """ Run the suite of tests for code in the module (this file). """
    test(day_add("Sunday", 4) == "Thursday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday") 
    test(day_add("Sunday", -1) == "Saturday") 
    test(day_add("Sunday", -7) == "Sunday") 
    test(day_add("Tuesday", -100) == "Sunday") 
    

def turn_clockwise(cp):
    """ Compass point, cp, turn clockwise one compass point, np """
    #np = cp + 90                # Original idea 
    N = "N"     # 360
    E = "E"     # 90
    S = "S"     # 180
    W = "W"     # 270
    if cp == "W":
        return "N"
    elif cp == "N":
        return "E"
    elif cp == "E":
        return "S"
    elif cp == "S":
        return "W"
    else:
        return None 


def day_name(day_num):
    """ Covert integer 0 to 6 to name of day """
    if day_num == 0:
        return "Sunday"
    elif day_num == 1: 
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    elif day_num == 4:
        return "Thursday"
    elif day_num == 5:
        return "Friday"
    elif day_num == 6:
        return "Saturday"
    else:
        return None 
    

def day_num(name_of_day):
    """ Covert name of day to an integer 0 to 6 """
    if name_of_day == "Sunday":
        return 0
    elif name_of_day == "Monday": 
        return 1
    elif name_of_day == "Tuesday":
        return 2
    elif name_of_day == "Wednesday":
        return 3
    elif name_of_day == "Thursday":
        return 4
    elif name_of_day == "Friday":
        return 5
    elif name_of_day == "Saturday":
        return 6
    else:
        return None 


def day_add(name_of_day, l):
    """ Take day name & delta argument (# days) & return resulting day name """
    x = l % 7 
    y = day_num(name_of_day) # day_num(name_of_day)
    z = x + y
    if z >= 7:
        return day_name(z - 7)
    else: 
        return day_name(z)


# print(day_add("Thursday", -3))

test_suite()                            # Here us the call to run the tests 


#Logical Oppositites

#Operator    Logical Opposite
#==          !=
#!=          ==
#<           >=
#<=          >
#>           <=
#>=          <

# de Morgans Laws / Simplification Laws :  
# not (x and y) == (not x) or (not y)
# not (x or y) == (not x) and (not y)

# Boolean and operators:

# x and False == False
# False and x == False
# y and x == x and y
# x and True == x
# True and x == x
# x and x == x
#
# Boolean or  operators:
#
# x or False == x
# False or x == x
# y or x == x or y
# x or True == True
# True or x == True
# x or x == x

# Boolean not operators:
#
# not (not x) == x
