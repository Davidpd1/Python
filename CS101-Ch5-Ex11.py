# David Powis-Dow CS 101:Python 
# 2016-1-16 v0.1
# Chapter 5 : Exercise 8 - Turtle Bar Chart  

def is_right_angle(a, b, c):
    if abs((a ** 2) + (b ** 2) - (c ** 2)) < 0.000001:      # If x is approximately equal to y  
        print(True) 
    else:
        print(False) 

is_right_angle(4.0, 4.0, 6.4)



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
