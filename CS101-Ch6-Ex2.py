# David Powis-Dow CS 101:Python 
# 2016-1-21 v0.1
# Chapter 6 : Exercise 1 - N, E, S, W  Clockwise Rotation

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
    test(day_num("Sunday") == 0)
    test(day_num("Monday") == 1)
    test(day_num("Tuesday") == 2)
    test(day_num("Wednesday") == 3)
    test(day_num("Thursday") == 4)
    test(day_num("Friday") == 5)
    test(day_num("Saturday") == 6) 
    test(day_num(42) == None)
    
 

def turn_clockwise(cp):
    """ Compass point, cp, turn clockwise one compass point, np """
    #np = cp + 90                # Original idea 
    if cp == "W":
        return "N"
    elif cp == "N":
        return "E"
    elif cp == "E":
        return S
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
    

def day_num(day_name):
    """ Covert name of day to an integer 0 to 6 """
    if day_name == "Sunday":
        return 0
    elif day_name == "Monday": 
        return 1
    elif day_name == "Tuesday":
        return 2
    elif day_name == "Wednesday":
        return 3
    elif day_name == "Thursday":
        return 4
    elif day_name == "Friday":
        return 5
    elif day_name == "Saturday":
        return 6
    else:
        return None 

N = "N"     # 360
E = "E"     # 90
S = "S"     # 180
W = "W"     # 270

# print(turn_clockwise("e"))

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
