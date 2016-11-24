# David Powis-Dow CS 101:Python 
# 2016-10-02 v0.1
# Chapter 2 Exercise 5: Compound Interest Calculation with Years Input 

# user_response = int(input("Please enter the number of years the money be compounded for?: "))
# population = int(input("Population of Toronto? "))

# var_t = (user_response)     # Number of Years 
var_P = (10000)             # Initial Sum Invested 
var_n = (12)                # Number Times Compounded per Year - Months 
var_r = (8/100)                 # Interest Rate 
var_t = float(input("Please enter the number of years the money be compounded for?: "))

#var_body = float(1 + (var_r / var_n)) # (1 + r/n)
#var_exponent = float(var_n * var_t) # nt 
#var_A = float(var_P * var_body) ** var_exponent

var_A = var_P * (1 + var_r / var_n) ** (var_n * var_t)

# P(1 + r/n)^nt
# A = P(1+r/n)**NT

print("Compounded amount is", var_A)
