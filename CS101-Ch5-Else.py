# David Powis-Dow CS 101:Python 
# 2016-12-17 v0.1
# Chapter 5 : Else 

import math

x = -3 

if x < 0:
    print("The negative number ", x, "is not valid here.") 
    x = 42
    print("I've decided to use the number 42 instead.")

print("The square root of ", x, "is", math.sqrt(x))
          

