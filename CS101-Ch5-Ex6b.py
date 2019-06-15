# David Powis-Dow CS 101:Python 
# 2017-01-14 v0.1
# Chapter 5 : Exercise 6 - Grades   

#import math
#import turtle 

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
#xs2 = [int(a) for a in xs] 

for i in xs:
    if i >= 75 and i <= 100:
        print("You earned a First.")
    elif i >= 70 and i < 75:
        print("You earned an Upper Second.")
    elif i >= 60 and i < 70:
        print("You earned a Second.")
    elif i >= 50 and i < 60:
        print("You earned a Third.")
    elif i >= 45 and i < 50:
        print("You earned a F1 Supp.")
    elif i >= 40 and i < 45:
        print("You earned a F2.")
    elif i < 40:
        print("You earned a F3.")
    pass 

# begin = int(input("What number day does the stay begin on?[0-6] "))
# length = int(input("How long is the stay in days? ")) 

# ending_day = (((begin + length) % 7) - 1)     # Minus 1 because the number scales differ. (0-6 vs 1-7)

#grade = convGrade(xs)

#print(grade)
    
# wn.mainloop()           

#Logical Oppositites

# Truth Tables
# AND
# a       b       a and b
# False   False   False
# False   True    False
# True    False   False
# True    True    True
# OR
# a       b       a or b
# F       F       F
# F       T       T
# T       F       T
# T       T       T
# NOT
# a       not a
# F       T
# T       F

#Operator    Logical Opposite
#==          !=
#!=          ==
#<           >=
#<=          >
#>           <=
#>=          <

# de Morgans Laws / Simplification Laws :  
# not (x and y) == (not x) or (not y)
# not (x or y) == (not x) and (not y)

# Boolean and operators:

# x and False == False
# False and x == False
# y and x == x and y
# x and True == x
# True and x == x
# x and x == x
#
# Boolean or  operators:
#
# x or False == x
# False or x == x
# y or x == x or y
# x or True == True
# True or x == True
# x or x == x

# Boolean not operators (two NOT operators cancel each other):
# 
# not (not x) == x
