# David Powis-Dow CS 101:Python 
# 2016-11-22 v0.1
# Chapter 4 : Turtle Draw Rectangle Function  

import turtle

#w = 50
#h = 75

def draw_rectangle(t, w, h):         # """Make turtle t draw a rectangle of width w and height h."""
    """Make turtle t draw a rectangle of width w and height h."""
    for i in range (2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        
wn = turtle.Screen()            # Set-up the window and its attributes 
wn.bgcolor("lightgreen") 
wn.title("Tess Meets A Rectangle Function")

t = turtle.Turtle()          # Create Tess 
t.pensize(3)

size = 20                       # size of the smallest square 
for i in range(1):
    w = 50                      # Increase the size for next time 
    h = 75                      # Move Tess along a little 
    draw_rectangle(t, w, h)
    
wn.mainloop()
    



