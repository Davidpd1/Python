# David Powis-Dow CS 101:Python 
# 2016-12-17 v0.1
# Chapter 5 : Turtle Bar Chart  

#import math
import turtle 

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()              # This is the fill color beginning
    t.left(90)
    t.forward(height)           # Draw up the left side
    t.write(' ' + str(height))  # Print the value
    t.right(90)
    t.forward(40)               # Width of bar, along the top
    t.right(90)
    t.forward(height)           # And down again!
    t.left(90)                  # Put the turtle facing the way we found it.
    t.end_fill()                # This is the fill color end 
    t.penup()
    t.forward(10)               # Leave a small gap after each bar
    t.pendown()
wn = turtle.Screen()            # Setup windows and its attribues
wn.bgcolor("lightgreen")

tess = turtle.Turtle()          # Create tess and some attributes
tess.pensize(3)
tess.color("blue", "red")

xs = [48, 117, 200, 240, 160, 260, 220]

for a in xs:                    # Assume xs and tess are ready 
           draw_bar(tess, a)
           
wn.mainloop()           

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
