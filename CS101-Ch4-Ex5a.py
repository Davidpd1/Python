# David Powis-Dow CS 101:Python 
# 2016-12-03 v0.1
# Chapter 4 : Exercise Turtle Functions    

import turtle

def make_window (colr, ttle):
    """
      Set up the window with the given background colar and title.
      Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle (colr, pensz):
    """
      Set up a given turtle with a give color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(pensz)
    return t

def draw_spiralSquare_v1 (t, n, sz):
    """
      Create Turtle t of n sides and size sz polygon.  
    """
    for a in range(n):
        t.forward(sz)
        t.left(90)
        sz = sz + 4
    return t

wn = make_window("azure", "Incresing Squares")
tess = make_turtle("hotpink", 2)
#sq_increment = 20                       # Set the increment for increasing the size of the square
draw_spiralSquare_v1(tess, 80, 5)

wn.mainloop()
    
#alex = make_turtle("black", 1)
#dave = make_turtle("yellow", 2)



