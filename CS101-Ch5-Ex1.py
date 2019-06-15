# David Powis-Dow CS 101:Python 
# 2017-01-14 v0.1
# Chapter 5 : Exercise 1 - Day of Week (Type Conversion)   

#import math
#import turtle 

#def draw_bar(t, height):
#    """ Get turtle t to draw one bar, of height. """

d = int(input("What number day is it?[0-6] "))

if d == 0:
    print("Today is Sunday.")
elif d == 1:
    print("Today is Monday.")
elif d == 2:
    print("Today is Tuesday.")
elif d == 3:
    print("Today is Wednesday.")
elif d == 4:
    print("Today is Thursday.")
elif d == 5:
    print("Today is Friday.")
elif d == 6:
    print("Today is Saturday.")
else:
    print("Please enter a number between 0 and 6.") 
    
# wn.mainloop()           

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
