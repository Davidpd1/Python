# David Powis-Dow CS 101:Python 
# 2016-10-29 v0.1
# Chapter 3 : Turtle 4 - For loop

# for f in ["Joe","Zoe","Brad","Angelina","Zuki","Thandi","Paris"]:
#     invite = "Hi " + f + ".  Please come to my party on Saturday!"
#     print(invite)

import turtle
wn = turtle.Screen()            # Set up the window and its attributes 
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()          # Create Tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()          # Create Alex

for j in range(3):              # Make Tess draw equilateral triangle 
    tess.forward(80)
    tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)                  # Complete the triangle

tess.right(180)                 # Turn Tess around
tess.forward(80)                # Move her away from the origin

# for c in ["yellow","red","purple","blue"]:
#     alex.color(c)
#     alex.forward(50)
#     alex.left(90)

clrs = ["yellow","red","purple","blue"]
for c in clrs:
    alex.color(c)
    alex.forward(50)
    alex.left(90) 
    
# for i in [0,1,2,3]:
# for i in range(4):              # Executes the body with i = 0 then 1, then 2, then 3
#    alex.forward(50)            # Make Alex draw a square
#    alex.left(90)

# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)

    wn.mainloop()



