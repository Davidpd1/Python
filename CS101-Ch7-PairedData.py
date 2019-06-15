# David Powis-Dow CS 101:Python 
# 2016-2-11 v0.1
# Chapter 7 : Tables

import sys
import math
import random

# def test(did_pass):
#    """ Print the result of a test. """
#    linenum = sys._getframe(1).f_lineno        # Get the caller's line number.
#m   if did_pass:
#        msg = "Test at line {0} ok.".format(linenum)
#    else:
#        msg = ("Test at line {0} FAILED.".format(linenum))
#    print(msg)
#
#    
# def test_suite():
#    """ Run the suite of tests for code in the module (this file). """
#    test(mysum([1, 2, 3, 4]) == 10)
#    test(mysum([1.25, 2.5, 1.75]) == 5.5)
#    test(mysum([1, -2, 3]) == 2)
#    test(mysum([ ]) == 0)
#    test(mysum(range(11)) == 55) # 11 is not included in the list.
#    test(sum_to(4) == 10)
#    test(sum_to(1000) == 500500)
#    test(num_digits(710) == 3)
#    test(num_zero_and_five_digits(1055030250) == 7)
#    test(num_zero_and_five_digits(0) == 1)
#    
#
# for f in ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
#     invitation = "Hi " + f + ". Please come to my party on Saturday!"
#     print(invitation)
#    
#
# def mysum(xs):
#    """ Sum all the numbers in the list xs, and return the total. """
#    running_total = 0
#    for x in xs:
#        running_total = running_total + x
#    return running_total
#
#
# def sum_to(n):
#    """ Return the sum of 1 +2 +3 ... n """
#    ss = 0
#    v = 1
#    while v <= n:
#        ss = ss + v
#        v = v + 1
#    return ss
#
#
# def seq3np1(n):
#     """ Print the 3n+1 sequence from n,
#         terminating whenit reaches I.
#     """
#     while n != 1:
#         print(n, end=", ")
#         if n % 2 == 0:          # n is even
#             n = n // 2
#         else:                   # n is odd
#             n = n * 3 + 1
#     print(n, end=".\n")
# 
#
# def num_digits(n):
#     count = 0
#     while n != 0:
#         count = count +1
#         n = n // 10
#     return count
#
#
#def num_zero_and_five_digits(n):
#    count = 0
#    while n > 0 :
#        digit = n % 10
#        if digit == 0 or digit == 5:
#            count = count + 1
#        n = n // 10
#    return count 
#print(num_digits(710))
# seq3np1(97)
#
#

#for x in range(13):     # Generate numbers 0 to 12
#    print(x, "\t", 2**x) 
    

#for i in range(1, 7):
#    print(2 * i, end="  ")
#print()


#def print_multiples(n):
#    for i in range(1, 7):
#        print(n * i, end="    ")
#    print()


#for i in range(1, 7):
#    print_multiples(i)
#
#
#def print_mult_table(n):
#    for i in range(1, 7):
#        print_multiples(i)
#
#
#print_mult_table(6)
#
#


#for i in (12, 16, 17, 24, 29):
#    if i % 2 == 1:      # If the number is odd
#        break           # immediately exit the loop
#    print(i)
#print("done")

# total = 0
#while True:
#    response = input("Enter the next number. (Leave blank to end)")
#    if response == "":
#        break
#    total += int(response)
#print("The total of the numbers you entered is", total)


#while True:
#    play_the_game_once()
#    response = input("Play again? (yes or no)")
#    if response != "yes":
#        break
#print("Goodbye!")


#rng = random.Random()      
#number = rng.randrange(1, 1000)        # Get random number between (1 and 1000)
#
#guesses = 0
#msg = ""
#
#while True:
#    guess = int(input(msg + "\nGuess my number between 1 and 1000: "))
#    guesses += 1
#    if guess > number:
#        msg += str(guess) + " is too high.\n"
#    elif guess < number:
#        msg += str(guess) + " is too low.\n"
#    else:
#        break
#
#input("\b\nGreat, you got it in {0} guesses!\n\n".format(guesses))
#    
#
#
#


#for i in [12, 16, 17, 24, 29, 30]:
#    if i % 2 == 1:                  # If the number is odd
#        continue                    # Don't process it
#    print(i)
#print("Done!")


#def print_mult_table(high):
#    for i in range(1, high+1):
#        print_multiples(i)


#def print_multiples(n, high):
#    for i in range(1, high+1):
#        print(n * i, end="  ")
#    print()
#
#
#def print_mult_table(high):
#    for i in range(1, high+1):
##        print_multiples(i, high)
##        print_multiples(i, i+1)
#        print_multiples(i, i)

#print_mult_table(7)

year_born = ("Paris Hilton", 1981)
celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Beiber", 1994)]

#print(len(celebs))

for (nm, yr) in celebs:
    if yr < 1980:
        print(nm)

        





#test_suite()                            # Here us the call to run the tests
#
#
#
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
