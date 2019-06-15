# David Powis-Dow CS 101:Python 
# 2016-12-03 v0.1
# Chapter 4 : Turtle Functions:    

def make_window (colr, ttle):
    """
      Set up the window with the given background colar and title.
      Returns the new window.
    """

    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle (colr, sz):
    """
      Set up a given turtle with a give color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen", "Tess and Alex Dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)
    
#wn.mainloop()
    



