# David Powis-Dow CS 101:Python 
# 2016-11-20 v0.1
# Chapter 4 : Turtle Draw Square Function  

import turtle

def draw_multicolor_square(t, sz):         # """Make turtle t draw a square of sz."""
    """Make turtle t draw a multicolor square of sz."""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
        
wn = turtle.Screen()            # Set-up the window and its attributes 
wn.bgcolor("lightgreen") 
wn.title("Tess Meets A Multicolor Square Function")

tess = turtle.Turtle()          # Create Tess 
tess.pensize(3)

size = 20                       # size of the smallest square 
for i in range(15):
    draw_multicolor_square(tess, size)
    size = size + 10            # Increase the size for next time 
    tess.forward(10)            # Move Tess along a little 
    tess.right(18)              # and give her some turn
    
wn.mainloop()
    



