# David Powis-Dow CS 101:Python 
# 2016-1-21 v0.1
# Chapter 6 : Composition (calling one function from within another)    

# Compute the area of a circle
# given center points of xc and yc and the perimeter points of xp and yp 

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2) 

def area(radius):
    return 3.14159 * radius * radius
    
# def area2(xc, yc, xp, yp):
#    radius = distance(xc, yc, xp, yp)
#    result = area(radius)
#    return result 

def area2(xc,yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

print(area2(1, 2, 4, 6))

# radius = distance(xc, yc, xp, yp) 

# result = area(radius)
# return result



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
