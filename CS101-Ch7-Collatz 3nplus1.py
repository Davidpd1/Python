# David Powis-Dow CS 101:Python 
# 2016-1-26 v0.1
# Chapter 7 : Collatz 3n + 1

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
    test(mysum([1, 2, 3, 4]) == 10)
    test(mysum([1.25, 2.5, 1.75]) == 5.5)
    test(mysum([1, -2, 3]) == 2)
    test(mysum([ ]) == 0)
    test(mysum(range(11)) == 55) # 11 is not included in the list.
    test(sum_to(4) == 10)
    test(sum_to(1000) == 500500)


#for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#    invitation = "Hi " + f + ". Please come to my party on Saturday!"
#    print(invitation)
    

def mysum(xs):
    """ Sum all the numbers in the list xs, and return the total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total


def sum_to(n):
    """ Return the sum of 1 +2 +3 ... n """
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v + 1
    return ss


def seq3np1(n):
    """ Print the 3n+1 sequence from n,
        terminating whenit reaches I.
    """
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:          # n is even
            n = n // 2
        else:                   # n is odd
            n = n * 3 + 1
    print(n, end=".\n")


seq3np1(97)
# test_suite()                            # Here us the call to run the tests



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
