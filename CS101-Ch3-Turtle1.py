# David Powis-Dow CS 101:Python 
# 2016-10-16 v0.1
# Chapter 3 : Turtle 1

import turtle                   # Allows us to use turtles 
wn = turtle.Screen()            # Create a plyground for turtles
alex = turtle.Turtle()          # Create a turtle, assign to Alex 

# wn.bgcolor("lightgreen")
# wn.title("Tess & Alex")

# tess = turtle.Turtle()          # Create Tess and set some attributes
# tess.color(("hotpink")
# tess.pensize(5)

# tess.forward(80)                # Make Tess draw equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)                  # Complete the triangle

# tess.right(180)                 # Turn Tess around
# tess.forward(80)                # Move her away from the origin


alex.forward(50)                  # Tell Alex to move forward by 50 units 
alex.left(90)                     # Tell Alex to turn left by 90 degrees 
alex.forward(30)                  # Complete the second side of the rectangle 
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

turtle.exitonclick()

wn.mainloop()
 
