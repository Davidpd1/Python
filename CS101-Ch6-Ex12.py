# David Powis-Dow CS 101:Python 
# 2016-1-21 v0.1
# Chapter 6 : Exercise 12 - Hypotenuse function

import sys
import math

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
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)
    test(days_in_month("July") == 31)
    test(days_in_month("february") == None)
    test(to_secs(2, 30, 10) == 9010)
    test(to_secs(2, 0, 0) == 7200)
    test(to_secs(0, 2, 0) == 120)
    test(to_secs(0, 0, 42) == 42)
    test(to_secs(0, -10, 10) == -590)
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)
    test(compare(5, 4) == 1)
    test(compare(7, 7) == 0)
    test(compare(2, 3) == -1)
    test(compare(42, 1) == 1)
    test(hypotenuse(3, 4) == 5.0)
    test(hypotenuse(12, 5) == 13.0)
    test(hypotenuse(24, 7) == 25.0)
    test(hypotenuse(9, 12) == 15.0)
    test(slope(5, 3, 4, 2) == 1.0)
    test(slope(1, 2, 3, 2) == 0.0)
    test(slope(1, 2, 3, 3) == 0.5)
    test(slope(2, 4, 1, 2) == 2.0)
    test(intercept(1, 6, 3, 12) == 3.0)
    test(intercept(6, 1, 1, 6) == 7.0)
    test(intercept(4, 6, 12, 8) == 5.0)
    

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


def days_in_month(name_of_month):
    """ Takes name of month, returns number of days - ignore leap """
    if name_of_month == "January":
        return 31
    elif name_of_month == "February":
        return 28
    elif name_of_month == "March":
        return 31
    elif name_of_month == "April":
        return 30
    elif name_of_month == "May":
        return 31
    elif name_of_month == "June":
        return 30
    elif name_of_month == "July":
        return 31 
    elif name_of_month == "August":
        return 31
    elif name_of_month == "September":
        return 30
    elif name_of_month == "October":
        return 31
    elif name_of_month == "November":
        return 30
    elif name_of_month == "December":
        return 31
    else:
        return None 


def to_secs(num_h, num_m, num_s):
    """ Converts hours, minutes & seconds to overall seconds """
    s = 1
    m = 60
    h = 3600
    x = (num_h * h) ++ (num_m * m) ++ (num_s * 1)
    return int(x)


def hours_in(ts):
    """ Returns whole integer of hours from overall seconds """
    s = 1
    m = 60
    h = 3600
    x = ts / h
    return int(x)


def minutes_in(ts):
    """ Returns whole integer number of minutes left after hours removed """
    s = 1
    m = 60
    h = 3600
    rh = ts % h
    rm = rh / m
    return int(rm) 


def seconds_in(ts):
    s = 1
    m = 60
    h = 3600
    rh = ts % h
    rm = rh % m
    rs = rm / s
    return int(rs) 


def compare(a, b):
    """ Compare returns 1 if a > b; 0 if ==; -1 if a < b """
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1
    else:
        return None


def hypotenuse(a, b):
    """ Returns length of hypotenuse of right triangle given two legs """
    hypo = math.sqrt((a**2) + (b**2))
    return hypo


def slope(x1, y1, x2, y2):
    """ Returns slope of line thru points x1,y1 - x2,y2 """
    m = (y2-y1)/(x2-x1)
    return m


def intercept(x1, y1, x2, y2):
    """ Returns y-intercept of lines thru points x1,y1 and x2,y2 (y=mx+b)"""
    m = slope(x1, y1, x2, y2)
    b = m * -x1 + y1
    return b
    
# print(seconds_in(9010))

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
