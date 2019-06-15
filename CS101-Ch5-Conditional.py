# David Powis-Dow CS 101:Python 
# 2016-12-16 v0.1
# Chapter 5 : Conditional execution

x = 3 

if x % 2 == 0:
    print(x, "is even.")
    print("Did you know that 2 is the only even number that is prime?")
else:
    print(x, "is odd.")
    print("Did you know that multiplying two odd numbers " + "always gives an odd result?")
    

# Operators and evaluation order
# , [...] {...} '...'               Tuple, list & dict. creation; string conv.
# s[i] s[i:j] s.attr f(...)         Indexing & slicing; attributes, function calls
# +x, -x, ~x                        Unary operators
# x**y                              Power
# x*y x/y x%y                       Multiplication, division, modulo
# x+y x-y                           Addition, subtraction
# x&y                               Bitwise "and"; also intersection of sets
# x^y                               Bitwise "or"; also union of sets
# x<y x<=y x>y x>=y x==y x!=y x<>y  Comparison
# x is y  x is not y                Identity
# x is s  x not in s                Membership
# not x                             Boolean negation
# x and y                           Boolean and
# x or y                            Boolean or
# lambda args:expr                  Anonymous function

# Alternate names are defined in module operator (e.g. __add__ and add for +)
# Most operators are overridable



