# David Powis-Dow CS 101:Python 
# 2016-1-16 v0.1
# Chapter 5 : Exercise 8 - Turtle Bar Chart  

def find_hypot(a, b):
    c = a + b 
    h = c ** 0.5
    print(h)

find_hypot(4, 5)

# print(find_hypot) 

    
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
