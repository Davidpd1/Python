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

def make_nested_square (t, numbr, sq_increment):
    """
      Create numbr of squares of sqsz.  
    """
    for n in range(numbr):
        for i in range(4):
            t.forward(sq_increment)
            t.left(90)
        t.penup()
        t.back(10)
        t.right(90)
        t.forward(10)
        t.left(90)
        t.pendown()
        sq_increment = sq_increment + 20
    return t
      
wn = make_window("azure", "Repeating Squares")
tess = make_turtle("hotpink", 5)
#sq_increment = 20                       # Set the increment for increasing the size of the square
make_nested_square(tess, 5, 20)

wn.mainloop()
    
#alex = make_turtle("black", 1)
#dave = make_turtle("yellow", 2)



