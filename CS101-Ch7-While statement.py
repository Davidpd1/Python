# David Powis-Dow CS 101:Python 
# 2018-3-5 v0.1
# Chapter 7 : While Statement

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

def sum_to(n):
    """ Return the sum of 1 + 2 + 3 ... n. """
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss 

#" Add tests like these to your test suite ...
test(sum_to(4) == 10)
test(sum_to(1000) == 500500)

    

#test_suite()                            # Here us the call to run the tests



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
