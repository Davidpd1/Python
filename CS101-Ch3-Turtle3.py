# David Powis-Dow CS 101:Python 
# 2016-10-16 v0.1
# Chapter 3 : Turtle 3

import turtle
wn = turtle.Screen()            # Set up the window and its attributes 
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()          # Create Tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()          # Create Alex

tess.forward(80)                # Make Tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                  # Complete the triangle
            
tess.right(180)                 # Turn Tess around
tess.forward(80)                # Move her away from the origin

alex.forward(50)                # Make Alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
