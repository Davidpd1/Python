# David Powis-Dow CS 101:Python 
# 2016-1-21 v0.1
# Chapter 6 : Boolean Functions (used to hide complicated test inside functions)

# 
#  

# def is_divisible(x, y):
#    """ Test if x is exactly divisible by y """
#    if x % y == 0:
#        return True
#    else:
#        return False

def is_divisible(x, y):
    return x % y == 0 

print(is_divisible(8, 4))

# boolean function are often used in conditional statements:
# if is_divisible(x, y):
#     ... # Do something ...
# else:
#     ... # Do something else ...
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
