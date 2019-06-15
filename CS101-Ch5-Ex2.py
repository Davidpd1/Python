# David Powis-Dow CS 101:Python 
# 2017-01-14 v0.1
# Chapter 5 : Exercise 2 - Length of Stay and Ending Day   

#import math
#import turtle 

#def draw_bar(t, height):
#    """ Get turtle t to draw one bar, of height. """

# def ending_day(begin,length):
#     """ Determine the day of the week the stay ends on. """
#     ((begin + length)-1) % 7 == x  

def day_of_wk(ending_day):
    """ Determine the day of the week. Print a str. """
    if ending_day == 0:
        print("You will return on a Sunday.")
    elif ending_day == 1:
        print("You will return on a Monday.")
    elif ending_day == 2:
        print("You will return on a Tuesday.")
    elif ending_day == 3:
        print("You will return on a Wednesday.")
    elif ending_day == 4:
        print("You will return on a Thursday.")
    elif ending_day == 5:
        print("You will return on a Friday.")
    elif ending_day == 6:
        print("You will return on a Saturday.")
    return

begin = int(input("What number day does the stay begin on?[0-6] "))
length = int(input("How long is the stay in days? ")) 

ending_day = (((begin + length) % 7) - 1)     # Minus 1 because the number scales differ. (0-6 vs 1-7)

day_of_wk(ending_day) 

    
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
