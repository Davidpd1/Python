# David Powis-Dow CS 101:Python 
# 2016-10-30 v0.1
# Chapter 3 : Exercise 3 - Five-pointed Star 

import turtle
wn = turtle.Screen()            # Set up the window and its attributes 
wn.bgcolor("red")
wn.title("Five-Point Star")

alex = turtle.Turtle()          # Create Alex and set some attributes

alex.shape("turtle")            # “out of the box” are arrow, blank, circle, classic, square, triangle, turtle.
alex.color("azure")
alex.speed(10)                  # 1 is slowest, 10 is fastest.  0 is animation off and fast. 
alex.pensize(5)

# alex.penup()                    # This is new
# size = 20

for i in range(5):              # Make Tess draw equilateral triangle
    alex.right(144)              # ... and turn Alex     
    alex.forward(100)          # Move Alex along

# alex.color("black") 

wn.mainloop()
    
