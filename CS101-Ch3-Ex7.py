# David Powis-Dow CS 101:Python 
# 2016-11-20 v0.1
# Chapter 3 : Exercise 6 - Turtle Drunk Pirate  

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
size = 20

for dp in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    alex.forward(100)
    alex.left(dp)




