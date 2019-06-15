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

def draw_poly (t, n, sz):
    """
      Create t Turtle of n sides and sz size polygon.  
    """
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
    return t
def draw_equitriangle (t, sz):
    """
      Create an equilateral triangle of size sz.
    """
    draw_poly(t, 3, sz)
    return t

wn = make_window("azure", "Repeating Squares")
tess = make_turtle("hotpink", 5)
draw_equitriangle(tess, 60)
#draw_poly(tess, 8, 50)

wn.mainloop()
    
#alex = make_turtle("black", 1)
#dave = make_turtle("yellow", 2)



