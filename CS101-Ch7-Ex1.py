# David Powis-Dow CS 101:Python 
# 2016-2-12 v0.1
# Chapter 7 : Exercise 1: Function to count odd numbers in a list

import sys
import math
import random

# def test(did_pass):
#    """ Print the result of a test. """
#    linenum = sys._getframe(1).f_lineno        # Get the caller's line number.
#    if did_pass:
#        msg = "Test at line {0} ok.".format(linenum)
#    else:
#        msg = ("Test at line {0} FAILED.".format(linenum))
#    print(msg)
#
#    
# def test_suite():
#    """ Run the suite of tests for code in the module (this file). """
#    test(mysum([1, 2, 3, 4]) == 10)
#    test(mysum([1.25, 2.5, 1.75]) == 5.5)
#    test(mysum([1, -2, 3]) == 2)
#    test(mysum([ ]) == 0)
#    test(mysum(range(11)) == 55) # 11 is not included in the list.
#    test(sum_to(4) == 10)
#    test(sum_to(1000) == 500500)
#    test(num_digits(710) == 3)
#    test(num_zero_and_five_digits(1055030250) == 7)
#    test(num_zero_and_five_digits(0) == 1)
#    
#

xs = (1, 2, 3, 4, 5, 6, 7, 8, 9)

def count_odd_num(xs):
    """ Function to count how many odd numbers are in a list. """ 
    count = 0
    for x in xs:
        if x % 2 != 0:
            count = count + 1
        else:
            continue
    print(count)


count_odd_num(xs)


#test_suite()                            # Here us the call to run the tests
#
#
#
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
