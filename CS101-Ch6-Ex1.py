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
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("E") == "S")
    test(turn_clockwise("S") == "W")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise("A") == "E")
    test(turn_clockwise("A") == "S")
    test(turn_clockwise("A") == "W")
    test(turn_clockwise("A") == "N")
    test(turn_clockwise(N) == "E")
    test(turn_clockwise(E) == "S")
    test(turn_clockwise(S) == "W")
    test(turn_clockwise(W) == "N")
    test(turn_clockwise(0) == "E")
    test(turn_clockwise(1) == "S")
    test(turn_clockwise(-1) == "W")
    test(turn_clockwise(42) == "N")
    
 

def turn_clockwise(cp):
    #np = cp + 90                # compass point cp plus 90 degrees equal to next compass point np
    if cp == W:
        return N
    elif cp == N:
        return E
    elif cp == E:
        return S
    elif cp == S:
        return W
    else:
        return "error"

N = "N"     # 360
E = "E"     # 90
S = "S"     # 180
W = "W"     # 270

# print(turn_clockwise(E))

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
