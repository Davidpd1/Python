# David Powis-Dow CS 101:Python 
# 2016-12-17 v0.1
# Chapter 5 : de Morgans Simplificiation Laws  

#import math

sword_charge = 0.9
shield_energy = 100 

#if not (sword_charge >= 0.90) and (shield_energy >= 100):
#    print("Your attack has not effect, the dragon fries you to a crisp!")
#else:
#    print("The dragon crumples in a heap. You rescue the gorgeous princess!")

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
