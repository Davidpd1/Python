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

def make_square (numbr, sqsz):
    """
      Create numbr of squares of sqsz.  
    """
    for n in range(numbr):
        for i in range(4):
            tess.forward(sqsz)
            tess.left(90)
        tess.penup()
        tess.forward(sqsz + sqsz)
        tess.pendown()
    return tess
      
wn = make_window("azure", "Repeating Squares")
tess = make_turtle("hotpink", 5)
tess = make_square(5, 20)

wn.mainloop()
    
#alex = make_turtle("black", 1)
#dave = make_turtle("yellow", 2)



