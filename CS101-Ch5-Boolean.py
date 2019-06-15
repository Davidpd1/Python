# David Powis-Dow CS 101:Python 
# 2016-12-16 v0.1
# Chapter 5 : BooleanValues

x == y              # Produce True if ... x is equal to y
x != y              # ... x is not equal to y
x > y               # ... x is greater than y
x < y               # ... x is less than y
x >= y              # ... x is greater than or equal to y
x <= y              # ... x is less than or equal to y

# Truth Tables 

and

a       b       a and b 
False   False   False
False   True    False
True    False   False
True    True    True

or

a       b       a or b
False   False   False 
False   True    True
True    False   True
True    True    True

not

a       not a
False   True
True    False

Boolean Algebra

and 

x and False == False
False and x == False
y and x == y and x
x and True == x
x and x == x

or

x or False = x
False or x == x
y or x == x or y
x or True == True
x or x == x

not

not (not x) == x



