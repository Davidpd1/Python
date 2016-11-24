# David Powis-Dow CS 101:Python 
# 2016-11-20 v0.1
# Chapter 4 : Turtle Draw Square Function  

import turtle

def draw_square(t, sz):         # """Make turtle t draw a square of sz."""
    """Make turtle t draw a square of sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()            # Set-up the window and its attributes 
wn.bgcolor("lightgreen") 
wn.title("Alex Meets A Function")

alex = turtle.Turtle()          # Create Alex 
draw_square(alex, 50)           # Call the function to draw the square
wn.mainloop()
    



