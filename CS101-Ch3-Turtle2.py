# David Powis-Dow CS 101:Python 
# 2016-10-16 v0.1
# Chapter 3 : Turtle 2

import turtle
wn = turtle.Screen()            # Set up the window and its attributes 
wncolor = input("Please choose a background color: ")
wn.bgcolor(wncolor)
wn.title("Hello, Tess!")

tess = turtle.Turtle()          # Create Tess 

tesspencolor = input("Please choose a pen color: ")

tess.color(tesspencolor)

tesspensize = input("Please choose a pen size: ")
tesspensize = int(tesspensize)
tess.pensize(tesspensize)

tess.forward(50)                # Make Tess create an angle  
tess.left(120)
tess.forward(50)

wn.mainloop()
