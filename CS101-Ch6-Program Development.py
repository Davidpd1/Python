# David Powis-Dow CS 101:Python 
# 2016-1-19 v0.1
# Chapter 6 : Return Values    

# distance = sqrt (x2 - x1)sq + (y2 - y1)sq
# Pythagorean Theorem "The square of the hypotenuse
# (the side opposite the right angle) is equal to
# the sum of the squares of the other two sides
# Pythagorean Equation = a squared + b squared = c squared 
# Hypotenuse = can be found using the Pythagorean Theorem

# def distance(x1, y1, x2, y2):
#    return 0.0
#
# print(distance(1, 2, 4, 6))

# def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    dsquared = dx * dx + dy * dy
#   result = dsquared ** 0.5 
#    return result
#
#print(distance(1, 2, 4, 6))

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(distance(1, 2, 4, 6))



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
