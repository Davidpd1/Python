# David Powis-Dow CS 101:Python 
# 2016-12-11 v0.1
# Chapter 4 : Fruitful Function: Interest Rate Calculation   

def final_amt_v2 (principleAmount, nominalPercentageRate, numTimesPerYear, years):
    """
      Apply the compound interest formula to principleAmount
       to produce the final amount."""

    a = principleAmount * (1 + nominalPercentageRate/numTimesPerYear) ** (numTimesPerYear*years)
    return a                 # This is new, and makes the function fruitful. 

# Now that we have the function above let us call it. 
toInvest = float(input("How much do you want to invest?"))
fnl = final_amt_v2 (toInvest, 0.08, 12, 5)
print("At the end of the period you will have", fnl)
    
#wn.mainloop()
    



