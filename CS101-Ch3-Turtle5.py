    # David Powis-Dow CS 101:Python 
    # 2016-10-29 v0.1
    # Chapter 3 : Turtle 5 - Pen Up Pen Down 

    import turtle
    wn = turtle.Screen()            # Set up the window and its attributes 
    wn.bgcolor("red")
    wn.title("Hello, Kai")

    alex = turtle.Turtle()          # Create Alex and set some attributes

    alex.shape("turtle")            # “out of the box” are arrow, blank, circle, classic, square, triangle, turtle.
    alex.color("azure")
    alex.speed(10)                  # 1 is slowest, 10 is fastest.  0 is animation off and fast. 
    alex.pensize(5)

    alex.penup()                    # This is new
    size = 20

    for i in range(30):              # Make Tess draw equilateral triangle
        alex.stamp()                # Leave an impression on the canvas 
        size = size + 3              # Increase the size on every iteration 
        alex.forward(size)          # Move Alex along
        alex.right(24)              # ... and turn Alex     

    alex.color("black") 

    wn.mainloop()
