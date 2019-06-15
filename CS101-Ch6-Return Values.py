# David Powis-Dow CS 101:Python 
# 2016-1-19 v0.1
# Chapter 6 : Return Values   

# abs, pow, int, max, range 
# biggest = max(3, 7, 2, 5)
# x = abs(3 - 11) + 10

# def area(radius):
#    b = 3.14159 * radius**2
#    return b
#
# print(area(9))

# def area(radius):
#   return 3.14159 * radius * radius
#
# print(area(2))

# def absolute_value(x):
#    if x < 0:
#        return -x
#    else:
#        return x

# print(absolute_value(-10))

# def bad_absolute_value(x):
#    if x < 0:
#        return -x
#    elif x > 0:
#        return x

# print(bad_absolute_value(0))        # Ruturns "None" value because there is no "return" - dead code 

def find_first_2_letter_word(xs):           # Doesn't work except on first iteration
    for i in xs:
        if len(i) == 2:
            return i
        return ""

#xl = ["red", "yellow", "it", "drop", "stop", "at"]

print(find_first_2_letter_word(["on", "red", "yellow", "it", "drop", "stop", "at"])) 





#Logical Oppositites

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

# Boolean not operators:
#
# not (not x) == x
