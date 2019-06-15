# David Powis-Dow CS 101:Python 
# 2016-12-17 v0.1
# Chapter 5 : de Morgans Simplificiation Laws  

#import math

sword_charge = 0.9
shield_energy = 100 

# if not (sword_charge >= 0.90) and (shield_energy >= 100):
#     print("Your attack has not effect, the dragon fries you to a crisp!")
# else:
#     print("The dragon crumples in a heap. You rescue the gorgeous princess!")

# if (sword_charge < 0.90) or (shield_energy <100):
#     print("Your attack has no effect, the drag fries you to a crisp!")
# else:
#     print("The dragon crumples in a heap. You rescue the gorgeous princess!") 




if (sword_charge >= 0.90) and (shield_energy >= 100):
    print("Your attack has not effect, the dragon fries you to a crisp!")
else:
    print("The dragon crumples in a heap. You rescue the gorgeous princess!")


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
