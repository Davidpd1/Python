# David Powis-Dow CS 101:Python 
# 2016-10-31 v0.1
# Chapter 3 : Exercise 6 - Turtle Clock Face  

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen") 
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
size = 20


for t in range(12):         
    alex.penup()
    alex.forward(70)
    alex.pendown()
    alex.forward(15)
    alex.penup()
    alex.forward(15)
    alex.stamp()
    alex.backward(100)
    alex.right(30)
    




